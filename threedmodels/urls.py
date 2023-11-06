from django.urls import path
from . import views


app_name = "threedmodels"

urlpatterns = [
    path("", views.ThreedmodelListView.as_view(), name="object_list"),
    path("detail/(?P<pk>[0-9]+)", views.ThreedmodelDetail.as_view(), name="detail"),
    path("upload/", views.upload_file, name="upload_file"),
    path("update/(?P<pk>[0-9]+)", views.update_file, name="update_file"),
]
