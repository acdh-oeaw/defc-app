# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = "webpage"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about/", views.about, name="about"),
    path("imprint/", views.imprint, name="imprint"),
    path(
        "cukurici-movie/",
        views.cukurici_movie_content,
        name="cukurici_movie_content",
    ),
    path(
        "cukurici-movie-de/",
        views.cukurici_movie_german_version,
        name="cukurici_movie_german_version",
    ),
    path(
        "ada-tepe-movie/",
        views.ada_tepe_movie_content,
        name="ada_tepe_movie_content",
    ),
    path(
        "ada-tepe-movie-de/",
        views.ada_tepe_movie_german_version,
        name="ada_tepe_movie_german_version",
    ),
    path("terms-of-use/", views.terms_of_use, name="terms_of_use"),
    path("defc2rdf/", views.defc2rdf_demo, name="defc2rdf_demo"),
    path("mapping2cidoc/", views.mapping2cidoc, name="mapping2cidoc"),
    path("defc-thesaurus/", views.defc_thesaurus, name="defc-thesaurus"),
    path("chronology-table/", views.chronology_table, name="chronology-table"),
    path("blog/", views.blog_main, name="blog_main"),
    path("blog/post01/", views.blog_post_01, name="blog_post_01"),
    path("blog/post02/", views.blog_post_02, name="blog_post_02"),
    path("blog/post03/", views.blog_post_03, name="blog_post_03"),
    path("blog/post04/", views.blog_post_04, name="blog_post_04"),
    path("blog/post05/", views.blog_post_05, name="blog_post_05"),
    path("create/event/", views.EventCreate.as_view(), name="event_create"),
    path(
        "update/event/(?P<pk>[0-9]+)",
        views.EventUpdate.as_view(),
        name="event_update",
    ),
    path("list/event/", views.EventListViewAdmin.as_view(), name="event_list"),
    path(
        "delete/event/(?P<pk>[0-9]+)",
        views.EventDelete.as_view(),
        name="event_delete",
    ),
]
