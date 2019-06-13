from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
from .form import ArticlePostForm
from django.contrib.auth.models import User
import markdown
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from article_comment.models import Article_Comment
from article_comment.forms import CommentForm
# Create your views here.

def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    if search:
        if order =='total_views':
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            ).order_by('-total_views')
        else:
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )
    else:
        search = ''
        if order == 'total_views':
            article_list = ArticlePost.objects.all().order_by('-total_views')
        else:
            article_list = ArticlePost.objects.all()
            order = 'normal'
    paginator = Paginator(article_list,5)

    page = request.GET.get('page')

    articles = paginator.get_page(page)

    context = {'articles':articles,
               'order':order,
               'search':search
               }
    return render(request,'article/list.html', context)

def article_detail(request, id):
    article = ArticlePost.objects.get(id = id)
    article.total_views += 1
    article.save(update_fields=['total_views'])
    mkd = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    article.body = mkd.convert(article.body)
    comments = Article_Comment.objects.filter(article=id)
    comment_form = CommentForm()
    context = {
        'article': article,
        'toc':mkd.toc,
        'comments':comments,
        'article_comment_form':comment_form,
    }
    return render(request,'article/detail.html', context)

@login_required(login_url='/userprofile/login/')
def article_create(request):
    if request.method =='POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            return redirect('article:article_list')
        else:
            return HttpResponse("submit error! please try again!")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form':article_post_form}
        return render(request, 'article/create.html', context)

@login_required(login_url='/userprofile/login/')
def article_delete(request,id):
    article = ArticlePost.objects.get(id=id)
    if request.user != article.author:
        return HttpResponse("对不起，您无权删除这篇文章")
    article.delete()
    return redirect("article:article_list")


@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    article = ArticlePost.objects.get(id = id)
    if request.user != article.author:
        return HttpResponse("对不起，您无权修改这篇文章")
    if request.method =="POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect('article:article_detail',id=id)
        else:
            return HttpResponse('表单有误，请重新填写')
    else:
        article_post_form = ArticlePostForm()
        context = {'article':article, 'article_post_form':article_post_form}
        return render(request, 'article/update.html', context)

