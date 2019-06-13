#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 16:43
# @Author  : ZD Liu

from django.urls import path
from . import views

app_name = 'usermanage'

urlpatterns = [
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('register/',views.user_register, name='register'),
    path('forget_pw/',views.user_register, name='forget_pw'),
]
