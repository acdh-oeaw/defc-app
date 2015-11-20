from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^province/$', views.DC_provinceListView.as_view(), name='province_list'),
url(r'^province/edit/(?P<pk>[0-9]+)$', views.edit_DC_provinceForm, name='edit_province'),
]