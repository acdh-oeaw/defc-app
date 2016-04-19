# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^synczotero/$', views.sync_zotero, name="synczotero"),
    url(r'^synczotero/result$', views.sync_zotero_action, name="synczotero_action")
]
