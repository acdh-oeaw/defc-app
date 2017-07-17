from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'download-sites/$', views.SiteDownloadView.as_view(), name='download-sites'),
    url(r'sites/$', views.SiteListView.as_view(), name='browse_sites'),
    url(r'download_results/$', views.download_results, name='download_results'),
    url(r'areas/$', views.AreaListView.as_view(), name='browse_areas'),
    url(r'finds/$', views.FindsListView.as_view(), name='browse_finds'),
    url(r'research_events/$', views.ResearchEventListView.as_view(), name='browse_researchevents'),
    url(r'interpretations/$', views.InterpretationListView.as_view(), name='browse_interpretations'),
]
