#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 18:36
# @Author  : ZD Liu
from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('post-comment/<int:post_id>/', views.post_comment, name='post_comment'),
    path('post-comment/<int:post_id>/<int:parent_comment_id>/', views.post_comment, name='comment_reply'),
]