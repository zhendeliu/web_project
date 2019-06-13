#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-28 20:00
# @Author  : ZD Liu

from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('', views.index, name='home'),
    path('list/', views.index, name='post_list'),
    path('bbs/<int:id>/', views.post_detail, name='post_detail'),
    path('write/', views.write_post, name='write_post'),
    path('del/<int:id>/', views.delete_post, name='delete_post'),
    path('update/<int:id>/', views.update_post, name='update_post'),

]