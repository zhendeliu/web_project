from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from bbs.models import MessagePost
from .forms import CommentForm
from .models import Comment

# Create your views here.
@login_required(login_url='/user/login/')
def post_comment(request, post_id, parent_comment_id=None):
    post = get_object_or_404(MessagePost,id=post_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                new_comment.parent_id = parent_comment.get_root().id
                new_comment.replt_to = parent_comment.user
                new_comment.save()
                return HttpResponse('200 OK')
            new_comment.save()
            return redirect(post)
        else:
            return HttpResponse("表单有误，请重新填写。")
    elif request.method == 'GET':
        comment_form = CommentForm()
        context = {
            'comment_form':comment_form,
            'post_id':post_id,
            'parent_comment_id':parent_comment_id
        }
        return render(request, 'comment/reply.html', context)
    else:
        return HttpResponse("仅接受POST请求")