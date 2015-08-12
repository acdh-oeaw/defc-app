from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^sites/$', views.IndexView.as_view(), name='site_list'),
url(r'^$', views.start_view, name="start"),
url(r'^sites/create/$', views.SiteCreate.as_view(), name="site_create"),
url(r'^sites/update/(?P<pk>[0-9]+)$', views.SiteUpdate.as_view(), name='site_update'),
]

#some change for git