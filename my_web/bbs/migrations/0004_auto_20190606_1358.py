# Generated by Django 2.2.1 on 2019-06-06 03:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_messagepost_total_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagepost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
