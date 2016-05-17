# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.homepage, name='homepage'),
url(r'^about/$', views.about, name='about'),
url(r'^imprint/$', views.imprint, name='imprint'),
url(r'^create/event/$', views.EventCreate.as_view(), name='event_create'),
url(r'^update/event/(?P<pk>[0-9]+)$', views.EventUpdate.as_view(), name='event_update'),
url(r'^list/event/$', views.EventListViewAdmin.as_view(), name='event_list'),
url(r'^delete/event/(?P<pk>[0-9]+)$', views.EventDelete.as_view(), name='event_delete')
]