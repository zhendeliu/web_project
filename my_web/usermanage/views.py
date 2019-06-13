from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request,user)
                return redirect('bbs:post_list')
            else:
                return HttpResponse('账号或密码错误，请重新输入')
        else:
            return HttpResponse('非法操作，请认真输入账号密码')
    elif request.method == 'GET':
        login_form = UserLoginForm()
        context = {'form':login_form}
        return render(request,'usermanage/login.html',context)
    else:
        return  HttpResponse('请使用get或post方式登陆')

def user_logout(request):
    logout(request)
    return redirect("bbs:post_list")

def user_register(request):
    if request.method =='POST':
        register_form = UserRegisterForm(data=request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('bbs:post_list')
        else:
            return HttpResponse("表单填写有误，请重新填写")
    elif request.method =="GET":
        register_form = UserRegisterForm()
        context = {'form':register_form}
        return render(request, 'usermanage/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求")