#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-04 16:19
# @Author  : ZD Liu

from django import forms
from .models import Article_Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Article_Comment
        fields = ['body']