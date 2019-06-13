#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-07 19:28
# @Author  : ZD Liu

from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('list/', views.index, name='resources_list'),
    # path('bbs/<int:id>/', views.resources_detail, name='resources_detail'),

]