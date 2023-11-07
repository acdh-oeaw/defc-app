import requests
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django_tables2 import SingleTableView, RequestConfig

from .forms import DC_provinceForm
from defcdb.models import DC_province, Site
from browsing.tables import SiteTable
from browsing.filters import SiteListFilter, MapListFilter
from browsing.forms import GenericFilterFormHelper, SpecificMapForm
from browsing.views import GenericListView


class SiteListFilterView(GenericListView):
    model = Site
    table_class = SiteTable
    template_name = "geolocation/site_map.html"
    filter_class = MapListFilter
    formhelper_class = SpecificMapForm

    def get_queryset(self, **kwargs):
        qs = Site.objects.filter(latitude__isnull=False)
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        lst_json = []
        sites = self.get_queryset().distinct()
       
        for x in sites:
            r = {
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(x.longitude), float(x.latitude)],
                },
                "type": "Feature",
                "properties": {"popupContent": "<strong>{}</strong>".format(x.name)},
                "id": x.pk,
            }
            lst_json.append(r)
        context["GeoJson"] = json.dumps(lst_json)
        return context


def site_map(request):
    sites = Site.objects.exclude(latitude__isnull=True)
    return render(request, "geolocation/site_map.html", {"sites": sites})


def showplaces(request):
    """a view to dispay all site objects on a leaflet map"""
    if request.method == "GET":
        context = {}
        context["site_list"] = Site.objects.exclude(latitude__isnull=True)
        return render(request, "geolocation/showplaces.html", context)
    else:
        pass


def showdistricts(request):
    """a view to generate a highmaps maps of districts in turkey"""
    context = {}
    context["province_list"] = DC_province.objects.exclude(lat__isnull=True)
    return render(request, "geolocation/districts_highmaps.html", context)


class DC_provinceListView(generic.ListView):
    template_name = "geolocation/list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        return DC_province.objects.all()


@login_required
def edit_DC_provinceForm(request, pk):
    """this view fetech geonames ID matching the districts/province´s name"""
    f = DC_province.objects.get(id=pk)
    if request.method == "GET":
        placeName = f.name
        root = "http://api.geonames.org/searchJSON?q="
        username = "&username=digitalarchiv"
        params = "&fuzzy=1&lang=de&maxRows=100"
        url = root + placeName + params + username
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            url = e
        response = r.text
        responseJSON = json.loads(response)
        responseJSON = responseJSON["geonames"]
        form = DC_provinceForm(instance=f)
        return render(
            request,
            "geolocation/edit_place.html",
            {"object": f, "form": form, "responseJSON": responseJSON},
        )
    else:
        form = DC_provinceForm(request.POST, instance=f)
        if form.is_valid():
            form.save()
        return redirect("geolocation:province_list")
