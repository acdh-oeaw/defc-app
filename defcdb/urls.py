# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
#add something...

urlpatterns = [
url(r'^$', views.start_view, name="start"),
url(r'^name/create/$', views.create_name, name='name_create'),
url(r'^site/$', views.SiteListView.as_view(), name='site_list'),
url(r'^site/create/$', views.create_site, name='site_create'),
url(r'^site/update/(?P<pk>[0-9]+)$', views.update_site, name='site_update'),
url(r'^site/delete/(?P<pk>[0-9]+)$', views.SiteDelete.as_view(), name='site_delete'),
url(r'^site/detail/(?P<pk>[0-9]+)$', views.SiteDetail.as_view(), name='site_detail'),
url(r'^finds/$', views.FindsListView.as_view(), name='finds_list'),
url(r'^finds/create/$', views.create_finds, name='finds_create'),
url(r'^finds/update/(?P<pk>[0-9]+)$', views.update_finds, name='finds_update'),
url(r'^finds/delete/(?P<pk>[0-9]+)$', views.FindsDelete.as_view(), name='finds_delete'),
url(r'^finds/detail/(?P<pk>[0-9]+)$', views.FindsDetail.as_view(), name='finds_detail'),
url(r'^area/$', views.AreaListView.as_view(), name='area_list'),
url(r'^area/create/$', views.create_area, name='area_create'),#url(r'^area/update/(?P<pk>[0-9]+)$', views.AreaUpdate.as_view(), name='area_update'),
url(r'^area/update/(?P<pk>[0-9]+)$', views.update_area, name='area_update'),
url(r'^area/delete/(?P<pk>[0-9]+)$', views.AreaDelete.as_view(), name='area_delete'),
url(r'^area/detail/(?P<pk>[0-9]+)$', views.AreaDetail.as_view(), name='area_detail'),
url(r'^period/$', views.PeriodListView.as_view(), name='period_list'),
url(r'^period/create/$', views.PeriodCreate.as_view(), name='period_create'),
url(r'^period/update/(?P<pk>[0-9]+)$', views.PeriodUpdate.as_view(), name='period_update'),
url(r'^period/delete/(?P<pk>[0-9]+)$', views.PeriodDelete.as_view(), name='period_delete'),
url(r'^period/detail/(?P<pk>[0-9]+)$', views.PeriodDetail.as_view(), name='period_detail'),
url(r'^researchevent/$', views.ResearchEventListView.as_view(), name='researchevent_list'),
# url(r'^researchevent/create/$', views.ResearchEventCreate.as_view(), name='researchevent_create'),
url(r'^researchevent/create/$', views.create_researchevent, name='researchevent_create'),
url(r'^researchevent/update/(?P<pk>[0-9]+)$', views.update_researchevent, name='researchevent_update'),
url(r'^researchevent/delete/(?P<pk>[0-9]+)$', views.ResearchEventDelete.as_view(), name='researchevent_delete'),
url(r'^researchevent/detail/(?P<pk>[0-9]+)$', views.ResearchEventDetail.as_view(), name='researchevent_detail'),
url(r'^interpretation/$', views.InterpretationListView.as_view(), name='interpretation_list'),
url(r'^interpretation/create/$', views.create_interpretation, name='interpretation_create'),
url(r'^interpretation/update/(?P<pk>[0-9]+)$', views.update_interpretation, name='interpretation_update'),
url(r'^interpretation/delete/(?P<pk>[0-9]+)$', views.InterpretationDelete.as_view(), name='interpretation_delete'),
url(r'^interpretation/detail/(?P<pk>[0-9]+)$', views.InterpretationDetail.as_view(), name='interpretation_detail'),
]
#class Interpretation must be added
#some change for git