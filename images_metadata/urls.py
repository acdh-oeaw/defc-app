# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = "images_metadata"

urlpatterns = [
    path("", views.ImageThesaurusListView.as_view(), name="object_list"),
    path("upload/", views.upload_file, name="upload_file"),
    path("update/(?P<pk>[0-9]+)", views.update_file, name="update_file"),
    path("detail/(?P<pk>[0-9]+)", views.ImageThesaurusDetail.as_view(), name="detail"
    ),
    path("public/",
        views.ImageThesaurusPublicListView.as_view(),
        name="public_object_list",
    ),
]
