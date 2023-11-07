# -*- coding: utf-8 -*-
from django.urls import path
from . import views

# add something...

app_name = "defcdb"

urlpatterns = [
    path("", views.start_view, name="start"),
    path("search", views.search_all, name="search_all"),
    path("name/create/", views.create_name, name="name_create"),
    path("exploreturkey/", views.turkey_map_view, name="turkey_map"),
    path("exploregreece/", views.greece_map_view, name="greece_map"),
    path("bibliography/", views.bibliography_view, name="bibliography"),
    path("site/create/", views.create_site, name="site_create"),
    path("site/update/<int:pk>", views.update_site, name="site_update"),
    path("site/delete/<int:pk>", views.SiteDelete.as_view(), name="site_delete"),
    path("site/detail/<int:pk>", views.SiteDetail.as_view(), name="site_detail"),
    path("finds/", views.FindsListView.as_view(), name="finds_list"),
    path("finds/create/", views.create_finds, name="finds_create"),
    path("finds/update/<int:pk>", views.update_finds, name="finds_update"),
    path(
        "finds/delete/<int:pk>",
        views.FindsDelete.as_view(),
        name="finds_delete",
    ),
    path(
        "finds/detail/<int:pk>",
        views.FindsDetail.as_view(),
        name="finds_detail",
    ),
    path("area/", views.AreaListView.as_view(), name="area_list"),
    path(
        "area/create/", views.create_area, name="area_create"
    ),  # url(r'^area/update/<int:pk>', views.AreaUpdate.as_view(), name='area_update'),
    path("area/update/<int:pk>", views.update_area, name="area_update"),
    path("area/delete/<int:pk>", views.AreaDelete.as_view(), name="area_delete"),
    path("area/detail/<int:pk>", views.AreaDetail.as_view(), name="area_detail"),
    path(
        "researchevent/",
        views.ResearchEventListView.as_view(),
        name="researchevent_list",
    ),
    # url(r'^researchevent/create/', views.ResearchEventCreate.as_view(), name='researchevent_create'),
    path(
        "researchevent/create/",
        views.create_researchevent,
        name="researchevent_create",
    ),
    path(
        "researchevent/update/<int:pk>",
        views.update_researchevent,
        name="researchevent_update",
    ),
    path(
        "researchevent/delete/<int:pk>",
        views.ResearchEventDelete.as_view(),
        name="researchevent_delete",
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
        "interpretation/create/",
        views.create_interpretation,
        name="interpretation_create",
    ),
    path(
        "interpretation/update/<int:pk>",
        views.update_interpretation,
        name="interpretation_update",
    ),
    path(
        "interpretation/delete/<int:pk>",
        views.InterpretationDelete.as_view(),
        name="interpretation_delete",
    ),
    path(
        "interpretation/detail/<int:pk>",
        views.InterpretationDetail.as_view(),
        name="interpretation_detail",
    ),
]
# class Interpretation must be added
# some change for git
