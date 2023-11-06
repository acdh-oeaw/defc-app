# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = "publicrecords"
urlpatterns = [
    path("site/", views.SiteListView.as_view(), name="site_list"),
    path("site/detail/(?P<pk>[0-9]+)", views.SiteDetail.as_view(), name="site_detail"),
    path("finds/", views.FindsListView.as_view(), name="finds_list"),
    path(
        "finds/detail/(?P<pk>[0-9]+)",
        views.FindsDetail.as_view(),
        name="finds_detail",
    ),
    path("area/", views.AreaListView.as_view(), name="area_list"),
    path("area/detail/(?P<pk>[0-9]+)", views.AreaDetail.as_view(), name="area_detail"),
    path(
        "researchevent/",
        views.ResearchEventListView.as_view(),
        name="researchevent_list",
    ),
    path(
        "researchevent/detail/(?P<pk>[0-9]+)",
        views.ResearchEventDetail.as_view(),
        name="researchevent_detail",
    ),
    path(
        "interpretation/",
        views.InterpretationListView.as_view(),
        name="interpretation_list",
    ),
    path(
        "interpretation/detail/(?P<pk>[0-9]+)",
        views.InterpretationDetail.as_view(),
        name="interpretation_detail",
    ),
]
