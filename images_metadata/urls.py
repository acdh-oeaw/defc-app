# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.ImageThesaurusListView.as_view(), name='object_list'),
]


#######add in main urls.py#########
#rl(r'^image_gallery/', include('images_metadata.urls', namespace="image_gallery")),