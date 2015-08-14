from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.start_view, name="start"),
url(r'^sites/$', views.SiteListView.as_view(), name='site_list'),
url(r'^sites/create/$', views.SiteCreate.as_view(), name='site_create'),
url(r'^sites/update/(?P<pk>[0-9]+)$', views.SiteUpdate.as_view(), name='site_update'),
url(r'^sites/delete/(?P<pk>[0-9]+)$', views.SiteDelete.as_view(), name='site_delete'),
url(r'^sites/detail/(?P<pk>[0-9]+)$', views.SiteDetail.as_view(), name='site_detail'),
url(r'^finds/$', views.FindsListView.as_view(), name='finds_list'),
url(r'^finds/create/$', views.FindsCreate.as_view(), name='finds_create'),
url(r'^finds/update/(?P<pk>[0-9]+)$', views.FindsUpdate.as_view(), name='finds_update'),
url(r'^finds/delete/(?P<pk>[0-9]+)$', views.FindsDelete.as_view(), name='finds_delete'),
url(r'^finds/detail/(?P<pk>[0-9]+)$', views.FindsDetail.as_view(), name='finds_detail'),
url(r'^settlement/$', views.SettlementListView.as_view(), name='settlement_list'),
url(r'^settlement/create/$', views.SettlementCreate.as_view(), name='settlement_create'),
url(r'^settlement/update/(?P<pk>[0-9]+)$', views.SettlementUpdate.as_view(), name='settlement_update'),
url(r'^settlement/delete/(?P<pk>[0-9]+)$', views.SettlementDelete.as_view(), name='settlement_delete'),
url(r'^settlement/detail/(?P<pk>[0-9]+)$', views.SettlementDetail.as_view(), name='settlement_detail'),
]

#some change for git