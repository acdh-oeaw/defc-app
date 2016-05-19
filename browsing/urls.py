from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'sites/$', views.SiteListView.as_view(), name='browse_sites'),
    url(r'areas/$', views.AreaListView.as_view(), name='browse_areas'),
    url(r'finds/$', views.FindsListView.as_view(), name='browse_finds'),
    url(r'research_events/$', views.ResearchEventListView.as_view(), name='browse_researchevents'),
    url(r'interpretations/$', views.InterpretationListView.as_view(), name='browse_interpretations'),
]
