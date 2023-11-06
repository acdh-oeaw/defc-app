# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = "bib"
urlpatterns = [
    path("synczotero/", views.sync_zotero, name="synczotero"),
    path("synczotero/result", views.sync_zotero_action, name="synczotero_action"),
]
