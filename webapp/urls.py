from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.IndexView.as_view(), name='index'),
#url(r'^create/$', views.create, name="create"),
]

#some change for git