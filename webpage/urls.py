# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.homepage, name='homepage'),
url(r'^about/$', views.about, name='about'),
url(r'^imprint/$', views.imprint, name='imprint'),
url(r'^movie/$', views.movie_content, name='movie_content'),
url(r'^movie-de/$', views.movie_german_version, name='movie_german_version'),
url(r'^terms-of-use/$', views.terms_of_use, name='terms_of_use'),
url(r'^defc2rdf/$', views.defc2rdf_demo, name='defc2rdf_demo'),
url(r'^blog/$', views.blog_main, name='blog_main'),
url(r'^blog/post01/$', views.blog_post_01, name='blog_post_01'),
url(r'^blog/post02/$', views.blog_post_02, name='blog_post_02'),
url(r'^create/event/$', views.EventCreate.as_view(), name='event_create'),
url(r'^update/event/(?P<pk>[0-9]+)$', views.EventUpdate.as_view(), name='event_update'),
url(r'^list/event/$', views.EventListViewAdmin.as_view(), name='event_list'),
url(r'^delete/event/(?P<pk>[0-9]+)$', views.EventDelete.as_view(), name='event_delete')
]