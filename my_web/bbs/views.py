from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MessagePost
from .forms import BbsPostForm
from django.contrib.auth.models import User
from comment.models import Comment
from comment.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

def index(request): # bbs_list
    # 数据--》按一定形式处理————》传递到html可访问

    posts_list =MessagePost.objects.all()
    paginator = Paginator(posts_list,8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts_list':posts}

    return render(request, 'bbs/list.html', context)

def post_detail(request,id):
    post = MessagePost.objects.get(id=id)
    post.total_views += 1
    post.save(update_fields=['total_views'])
    comments = Comment.objects.filter(post=id)
    comment_form = CommentForm()
    context = {'post':post,
               'comments':comments,
               'comment_form':comment_form,
               }
    return render(request,'bbs/detail.html',context)

@login_required(login_url='/user/login/')
def write_post(request):
    if request.method =='POST':
        post_form = BbsPostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = User.objects.get(id=request.user.id)
            new_post.save()
            return redirect('bbs:post_list')
        else:
            return  HttpResponse('表单有误，请重新填写')
    else:
        post_form = BbsPostForm()
        context = {'post_form':post_form}
        return render(request,'bbs/write_bbs.html',context)

@login_required(login_url='/user/login/')
def delete_post(request,id):
    post = MessagePost.objects.get(id=id)
    post.delete()
    return redirect('bbs:post_list')

@login_required(login_url='/user/login/')
def update_post(request, id):
    post = MessagePost.objects.get(id=id)
    if request.method == 'POST':
        post_form = BbsPostForm(data=request.POST)
        if post_form.is_valid():
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.save()
            return redirect('bbs:post_detail', id=id)
        else:
            return HttpResponse('表单内容填写有误，请重新填写！')

    else:
        post_form = BbsPostForm()
        context = {'post':post, 'post_form':post_form}
        return render(request, 'bbs/update.html',context)

