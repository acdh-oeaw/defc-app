# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^areatry/$', views.AreaTryListView.as_view(), name='areatry_list'),
url(r'^areatry/create/$', views.create_area, name='areatry_create'),
url(r'^areatry/detail/(?P<pk>[0-9]+)$', views.AreaTryDetail.as_view(), name='areatry_detail'),
]