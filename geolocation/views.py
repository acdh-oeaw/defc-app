from django.shortcuts import render, redirect
from django.views import generic
import requests, re, json

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import  DC_provinceForm
from defcdb.models import DC_province, DC_region, DC_country, Site

#################################################################
#		geovisualization										#
#################################################################

def showplaces(request):
	context = {}
	context["province_list"] = DC_province.objects.filter(site__province__isnull=False).exclude(lat__isnull=True)
	#context["province_list"] = DC_province.objects.filter(site__province=DC_proince)
	context["region_list"] = DC_region.objects.all()
	context["country_list"] = DC_country.objects.all()
	context["site_list"] = Site.objects.all()
	return render(request, 'geolocation/showplaces.html', context)


#################################################################
#		list Views												#
#################################################################

class DC_provinceListView(generic.ListView):
	template_name = 'geolocation/list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		return DC_province.objects.all()


#################################################################
#		fetch GeoNamesView										#
#################################################################

@login_required
def edit_DC_provinceForm(request, pk):
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
		form = DC_provinceForm(instance = f)
		#form = DC_provinceFormForm({'geonames_id':123})
		return render(request, 'geolocation/edit_place.html',
			{'object':f, 'form':form, 'responseJSON':responseJSON}
			)
	else:
		form = DC_provinceForm(request.POST, instance=f)
		if form.is_valid():
			form.save()
		return redirect('geolocation:province_list')