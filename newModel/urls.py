from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.start_view, name="start"),
url(r'^site/$', views.SiteListView.as_view(), name='site_list'),
url(r'^site/create/$', views.SiteCreate.as_view(), name='site_create'),
url(r'^site/update/(?P<pk>[0-9]+)$', views.SiteUpdate.as_view(), name='site_update'),
url(r'^site/delete/(?P<pk>[0-9]+)$', views.SiteDelete.as_view(), name='site_delete'),
url(r'^site/detail/(?P<pk>[0-9]+)$', views.SiteDetail.as_view(), name='site_detail'),
# url(r'^finds/$', views.FindsListView.as_view(), name='finds_list'),
# url(r'^finds/create/$', views.FindsCreate.as_view(), name='finds_create'),
# url(r'^finds/update/(?P<pk>[0-9]+)$', views.FindsUpdate.as_view(), name='finds_update'),
# url(r'^finds/delete/(?P<pk>[0-9]+)$', views.FindsDelete.as_view(), name='finds_delete'),
# url(r'^finds/detail/(?P<pk>[0-9]+)$', views.FindsDetail.as_view(), name='finds_detail'),
url(r'^area/$', views.AreaListView.as_view(), name='area_list'),
url(r'^area/create/$', views.AreaCreate.as_view(), name='area_create'),
url(r'^area/update/(?P<pk>[0-9]+)$', views.AreaUpdate.as_view(), name='area_update'),
url(r'^area/delete/(?P<pk>[0-9]+)$', views.AreaDelete.as_view(), name='area_delete'),
url(r'^area/detail/(?P<pk>[0-9]+)$', views.AreaDetail.as_view(), name='area_detail'),
]

#some change for git