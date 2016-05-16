from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'sites/$', views.SiteListView.as_view(), name='browse_sites'),
]
