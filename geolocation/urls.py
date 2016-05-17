
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^districts/$', views.DC_provinceListView.as_view(), name='province_list'),
    url(r'^province/edit/(?P<pk>[0-9]+)$', views.edit_DC_provinceForm, name='edit_province'),
    url(r'^excavations_map/$', views.showplaces, name='showplaces'),
    url(r'^showdistricts/$', views.showdistricts, name='showdistricts'),
    url(r'^site/geojson/$', views.getGeoJson, name='getGeoJson'),
    url(r'^site/show/$', views.site_map, name='filter_sites'),
]
