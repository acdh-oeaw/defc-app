# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^site/$", views.SiteListView.as_view(), name="site_list"),
    url(
        r"^site/detail/(?P<pk>[0-9]+)$", views.SiteDetail.as_view(), name="site_detail"
    ),
    url(r"^finds/$", views.FindsListView.as_view(), name="finds_list"),
    url(
        r"^finds/detail/(?P<pk>[0-9]+)$",
        views.FindsDetail.as_view(),
        name="finds_detail",
    ),
    url(r"^area/$", views.AreaListView.as_view(), name="area_list"),
    url(
        r"^area/detail/(?P<pk>[0-9]+)$", views.AreaDetail.as_view(), name="area_detail"
    ),
    url(
        r"^researchevent/$",
        views.ResearchEventListView.as_view(),
        name="researchevent_list",
    ),
    url(
        r"^researchevent/detail/(?P<pk>[0-9]+)$",
        views.ResearchEventDetail.as_view(),
        name="researchevent_detail",
    ),
    url(
        r"^interpretation/$",
        views.InterpretationListView.as_view(),
        name="interpretation_list",
    ),
    url(
        r"^interpretation/detail/(?P<pk>[0-9]+)$",
        views.InterpretationDetail.as_view(),
        name="interpretation_detail",
    ),
]
