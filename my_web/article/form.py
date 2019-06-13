#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-04 15:46
# @Author  : ZD Liu
from django import forms
from .models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'body')