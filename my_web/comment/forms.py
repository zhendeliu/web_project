#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 18:35
# @Author  : ZD Liu
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']