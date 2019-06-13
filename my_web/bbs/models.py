from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class MessagePost(models.Model):
    # 作者（作为外键需要指定联级删除），标题，内容，创建时间，更新时间
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    content = RichTextUploadingField()

    total_views = models.PositiveIntegerField(default=0)

    created_time = models.DateTimeField(default=timezone.now)

    updated_time = models.DateTimeField(auto_now=True)

    #元数据定义（指定数据返回时的=一些格式）
    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bbs:post_detail',args=[self.id])

