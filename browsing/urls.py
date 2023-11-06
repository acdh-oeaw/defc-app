from django.urls import path
from . import views


app_name = "browsing"

urlpatterns = [
    path("download-sites/", views.SiteDownloadView.as_view(), name="download-sites"),
    path("download-areas/", views.AreaDownloadView.as_view(), name="download-areas"),
    path("download-finds/", views.FindsDownloadView.as_view(), name="download-finds"),
    path("download-research-events/",
        views.ResearchEventDownloadView.as_view(),
        name="download-research-events",
    ),
    path("download-interpretations/",
        views.InterpretationDownloadView.as_view(),
        name="download-interpretations",
    ),
    path("sites/", views.SiteListView.as_view(), name="browse_sites"),
    path("areas/", views.AreaListView.as_view(), name="browse_areas"),
    path("finds/", views.FindsListView.as_view(), name="browse_finds"),
    path("research_events/",
        views.ResearchEventListView.as_view(),
        name="browse_researchevents",
    ),
    path("interpretations/",
        views.InterpretationListView.as_view(),
        name="browse_interpretations",
    ),
]
