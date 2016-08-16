"""BTI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from news import views, urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index, name = 'index'),
    url(r'^editor/', views.editor, name='editor'),
    # url(r'^search/', views.search_show, name = 'search_show'),
    url(r'^search/(?P<pattern>[\W\w.@+-]*)/$', views.search, name = 'search'),
    url(r'^news/(?P<news_url>[\W\w.@+-]+)/$', views.share, name='share'),
    url(r'^section/(?P<section_id>\d+)/(?P<section_title>[\W\w.@+-]+)/$', views.section, name='section'),


    # url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^editor/', include('news.urls')),
]
