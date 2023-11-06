# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = "publicrecords"
urlpatterns = [
    path("site/", views.SiteListView.as_view(), name="site_list"),
    path("site/detail/<int:pk>", views.SiteDetail.as_view(), name="site_detail"),
    path("finds/", views.FindsListView.as_view(), name="finds_list"),
    path(
        "finds/detail/<int:pk>",
        views.FindsDetail.as_view(),
        name="finds_detail",
    ),
    path("area/", views.AreaListView.as_view(), name="area_list"),
    path("area/detail/<int:pk>", views.AreaDetail.as_view(), name="area_detail"),
    path(
        "researchevent/",
        views.ResearchEventListView.as_view(),
        name="researchevent_list",
    ),
    path(
        "researchevent/detail/<int:pk>",
        views.ResearchEventDetail.as_view(),
        name="researchevent_detail",
    ),
    path(
        "interpretation/",
        views.InterpretationListView.as_view(),
        name="interpretation_list",
    ),
    path(
        "interpretation/detail/<int:pk>",
        views.InterpretationDetail.as_view(),
        name="interpretation_detail",
    ),
]
