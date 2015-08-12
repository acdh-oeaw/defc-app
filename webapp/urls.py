from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^sites/$', views.IndexView.as_view(), name='site_list'),
url(r'^$', views.start_view, name="start"),
url(r'^sites/create/$', views.SiteCreate.as_view(), name="site_create"),
]

#some change for git