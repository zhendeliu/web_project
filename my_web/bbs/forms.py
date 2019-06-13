#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 13:08
# @Author  : ZD Liu

from django import forms
from .models import MessagePost
from ckeditor.fields import RichTextField

class BbsPostForm(forms.ModelForm):
    class Meta:
        model =MessagePost
        fields = {'title', 'content'}