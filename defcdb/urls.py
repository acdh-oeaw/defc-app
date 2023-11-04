# -*- coding: utf-8 -*-
from django.urls import path
from . import views

# add something...

app_name = 'defcdb'

urlpatterns = [
    path("$", views.start_view, name="start"),
    path("search", views.search_all, name="search_all"),
    path("name/create/$", views.create_name, name="name_create"),
    path("exploreturkey/$", views.turkey_map_view, name="turkey_map"),
    path("exploregreece/$", views.greece_map_view, name="greece_map"),
    path("bibliography/$", views.bibliography_view, name="bibliography"),
    path("site/$", views.SiteListView.as_view(), name="site_list"),
    path("site/create/$", views.create_site, name="site_create"),
    path("site/update/(?P<pk>[0-9]+)$", views.update_site, name="site_update"),
    path("site/delete/(?P<pk>[0-9]+)$", views.SiteDelete.as_view(), name="site_delete"
    ),
    path("site/detail/(?P<pk>[0-9]+)$", views.SiteDetail.as_view(), name="site_detail"
    ),
    path("finds/$", views.FindsListView.as_view(), name="finds_list"),
    path("finds/create/$", views.create_finds, name="finds_create"),
    path("finds/update/(?P<pk>[0-9]+)$", views.update_finds, name="finds_update"),
    path("finds/delete/(?P<pk>[0-9]+)$",
        views.FindsDelete.as_view(),
        name="finds_delete",
    ),
    path("finds/detail/(?P<pk>[0-9]+)$",
        views.FindsDetail.as_view(),
        name="finds_detail",
    ),
    path("area/$", views.AreaListView.as_view(), name="area_list"),
    path("area/create/$", views.create_area, name="area_create"
    ),  # url(r'^area/update/(?P<pk>[0-9]+)$', views.AreaUpdate.as_view(), name='area_update'),
    path("area/update/(?P<pk>[0-9]+)$", views.update_area, name="area_update"),
    path("area/delete/(?P<pk>[0-9]+)$", views.AreaDelete.as_view(), name="area_delete"
    ),
    path("area/detail/(?P<pk>[0-9]+)$", views.AreaDetail.as_view(), name="area_detail"
    ),
    path("researchevent/$",
        views.ResearchEventListView.as_view(),
        name="researchevent_list",
    ),
    # url(r'^researchevent/create/$', views.ResearchEventCreate.as_view(), name='researchevent_create'),
    path("researchevent/create/$",
        views.create_researchevent,
        name="researchevent_create",
    ),
    path("researchevent/update/(?P<pk>[0-9]+)$",
        views.update_researchevent,
        name="researchevent_update",
    ),
    path("researchevent/delete/(?P<pk>[0-9]+)$",
        views.ResearchEventDelete.as_view(),
        name="researchevent_delete",
    ),
    path("researchevent/detail/(?P<pk>[0-9]+)$",
        views.ResearchEventDetail.as_view(),
        name="researchevent_detail",
    ),
    path("interpretation/$",
        views.InterpretationListView.as_view(),
        name="interpretation_list",
    ),
    path("interpretation/create/$",
        views.create_interpretation,
        name="interpretation_create",
    ),
    path("interpretation/update/(?P<pk>[0-9]+)$",
        views.update_interpretation,
        name="interpretation_update",
    ),
    path("interpretation/delete/(?P<pk>[0-9]+)$",
        views.InterpretationDelete.as_view(),
        name="interpretation_delete",
    ),
    path("interpretation/detail/(?P<pk>[0-9]+)$",
        views.InterpretationDetail.as_view(),
        name="interpretation_detail",
    ),
]
# class Interpretation must be added
# some change for git
