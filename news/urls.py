from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from . import views

urlpatterns = [
		url(r'^$',views.index, name = 'index'),
		url(r'^editor/', views.editor, name = 'editor'),
		# url(r'^search/', views.search_show, name = 'search_show'),
		url(r'^search/(?P<pattern>[\W\w.@+-]*)/$', views.search, name = 'search'),
		url(r'^news/(?P<news_url>[\W\w.@+-]+)/$', views.share, name='share'),
		url(r'^section/(?P<section_id>\d+)/(?P<section_title>[\W\w.@+-]+)/$', views.section, name='section'),
		]


