#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-04 16:17
# @Author  : ZD Liu

from django.urls import path
from . import views

app_name = 'article_comment'

urlpatterns = [
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
    path('post-comment/<int:article_id>/<int:parent_comment_id>', views.post_comment, name='comment_reply'),

]