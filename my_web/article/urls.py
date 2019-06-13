#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-04 15:33
# @Author  : ZD Liu

from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('',views.article_list, name = 'blog_home'),
    path('article-list/',views.article_list, name = 'article_list'),
    path('article-create/',views.article_create, name = 'article_create'),
    path('article-detail/<int:id>/',views.article_detail, name = 'article_detail'),
    path('article-delete/<int:id>/',views.article_delete, name = 'article_delete'),
    path('article-update/<int:id>/',views.article_update, name = 'article_update'),
]