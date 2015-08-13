from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^sites/$', views.IndexView.as_view(), name='site_list'),
url(r'^$', views.start_view, name="start"),
url(r'^sites/create/$', views.SiteCreate.as_view(), name="site_create"),
url(r'^sites/update/(?P<pk>[0-9]+)$', views.SiteUpdate.as_view(), name='site_update'),
url(r'^sites/delete/(?P<pk>[0-9]+)$', views.SiteDelete.as_view(), name='site_delete'),
url(r'^sites/detail/(?P<pk>[0-9]+)$', views.SiteDetail.as_view(), name='site_detail'),
]

#some change for git