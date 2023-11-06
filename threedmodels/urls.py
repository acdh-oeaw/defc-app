from django.urls import path
from . import views


app_name = "threedmodels"

urlpatterns = [
    path("", views.ThreedmodelListView.as_view(), name="object_list"),
    path("detail/<int:pk>", views.ThreedmodelDetail.as_view(), name="detail"),
    path("upload/", views.upload_file, name="upload_file"),
    path("update/<int:pk>", views.update_file, name="update_file"),
]
