# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
#url(r'^$', views.start_view, name="start"),
url(r'^$', views.VirtualObjectListView.as_view(), name='list'),
url(r'^upload/$', views.upload_file, name='upload_file'),
url(r'^detail/(?P<pk>[0-9]+)$', views.VirtualObjectDetail.as_view(), name='detail'),
]