"""my_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls',namespace='bbs')),
    path('favicon.ico', include('bbs.urls',namespace='fav')),
    path('blog/', include('article.urls',namespace='blog')),
    path('resources/', include('resources.urls',namespace='resources')),
    path('article_comment/', include('article_comment.urls',namespace='blog_comment')),
    path('', include('bbs.urls',namespace='home')),
    path('user/',include('usermanage.urls', namespace='usermanage')),
    path('comment/',include('comment.urls', namespace='comment')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)