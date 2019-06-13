from django.db import models
from django.contrib.auth.models import User
from article.models import ArticlePost
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Article_Comment(MPTTModel):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='article_comments',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='article_comments',
    )

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    reply_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article_replyers'
    )
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    # 替换 Meta 为 MPTTMeta
    # class Meta:
    #     ordering = ('created',)
    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.body[:20]


