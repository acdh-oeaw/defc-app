from django.urls import path
from . import views

urlpatterns = [
    path("districts/$", views.DC_provinceListView.as_view(), name="province_list"),
    url(
        r"^province/edit/(?P<pk>[0-9]+)$",
        views.edit_DC_provinceForm,
        name="edit_province",
    ),
    path("excavations_map/$", views.showplaces, name="showplaces"),
    path("showdistricts/$", views.showdistricts, name="showdistricts"),
    path("site/show/$", views.SiteListFilterView.as_view(), name="filter_sites"),
]
