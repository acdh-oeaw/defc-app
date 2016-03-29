# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ImageThesaurusListView.as_view(), name='object_list'),
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^update/(?P<pk>[0-9]+)$', views.update_file, name='update_file'),
]
