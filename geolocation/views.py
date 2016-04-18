import requests
import json
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import DC_provinceForm
from defcdb.models import DC_province, Site


def showplaces(request):
    """ a view to dispay all site objects on a leaflet map"""
    if request.method == "GET":
        context = {}
        context["site_list"] = Site.objects.exclude(latitude__isnull=True)
        return render(request, 'geolocation/showplaces.html', context)
    else:
        pass


def showdistricts(request):
    """ a view to generate a highmaps maps of districts in turkey"""
    context = {}
    context["province_list"] = DC_province.objects.exclude(lat__isnull=True)
    return render(request, 'geolocation/districts_highmaps.html', context)


class DC_provinceListView(generic.ListView):
    template_name = 'geolocation/list.html'
    context_object_name = 'object_list'

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
        url = root+placeName+params+username
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            url = e
        response = r.text
        responseJSON = json.loads(response)
        responseJSON = responseJSON['geonames']
        form = DC_provinceForm(instance=f)
        return render(request, 'geolocation/edit_place.html',
            {'object': f, 'form': form, 'responseJSON': responseJSON}
        )
    else:
        form = DC_provinceForm(request.POST, instance=f)
        if form.is_valid():
            form.save()
        return redirect('geolocation:province_list')
