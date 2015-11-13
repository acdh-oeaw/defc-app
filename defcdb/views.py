# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse, reverse_lazy
from rest_framework import viewsets

from .models import DC_province, DC_country, DC_region, Site, Area, Finds, Period, ResearchEvent, Interpretation, DC_period_datingmethod, DC_researchevent_researchtype
from .forms import form_user_login, AreaForm, ResearcheventForm, FindsForm, SiteForm, InterpretationForm
from .serializers import DC_countrySerializer, DC_regionSerializer, DC_provinceSerializer
from bib.models import Book


#####################################################
#				RESTApi views						#
#####################################################
class DC_countryViewSet(viewsets.ModelViewSet):
	queryset = DC_country.objects.all()
	serializer_class = DC_countrySerializer


class DC_regionViewSet(viewsets.ModelViewSet):
	queryset = DC_region.objects.all()
	serializer_class = DC_regionSerializer


class DC_provinceViewSet(viewsets.ModelViewSet):
	queryset = DC_province.objects.all()
	serializer_class = DC_provinceSerializer


#################################################################
#				views for ResearchEvent							#
#################################################################
class ResearchEventListView(generic.ListView):
	model = ResearchEvent
	template_name = 'defcdb/researchevent_list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class. 

	def get_queryset(self):
		return ResearchEvent.objects.order_by('id')

@login_required
def update_researchevent(request, pk):
	instance = get_object_or_404(ResearchEvent, id=pk)
	if request.method == "POST":
		form = ResearcheventForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
		return redirect('defcdb:researchevent_detail', pk=pk)
	else:
		form = ResearcheventForm(instance=instance)
		return render(request, 'defcdb/update_form.html', {'form': form})

@login_required
def create_researchevent(request):
	if request.method == "POST":
		form = ResearcheventForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('defcdb:researchevent_list')
	else:
		form = ResearcheventForm()
		return render(request, 'defcdb/create_researchevent.html', {'form':form})

# class ResearchEventCreate(CreateView):
# 	model = ResearchEvent
# 	fields = "__all__"
# 	template_name = "defcdb/create_researchevent.html"

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(ResearchEventCreate, self).dispatch(*args, **kwargs)


# class ResearchEventUpdate(UpdateView):
# 	model = ResearchEvent
# 	fields = "__all__"
# 	template_name = 'defcdb/update_form.html'

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(ResearchEventUpdate, self).dispatch(*args, **kwargs)


class ResearchEventDelete(DeleteView):
	model = ResearchEvent
	template_name = 'defcdb/confirm_delete.html'
	success_url = reverse_lazy('defcdb:researchevent_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ResearchEventDelete, self).dispatch(*args, **kwargs)


class ResearchEventDetail(DetailView):
	model = ResearchEvent
	def get_context_data(self, **kwargs):
		context = super(ResearchEventDetail, self).get_context_data(**kwargs)
		current_object = self.object
		context['researchtype_list'] = current_object.research_type.all()
		context['institution_list'] = current_object.institution.all()
		context['specialanalysis_list'] = current_object.special_analysis.all()
		context['reference_list'] = current_object.reference.all()
		return context


#################################################################
#				views for Period								#
#################################################################
class PeriodListView(generic.ListView):
	template_name = 'defcdb/period_list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class.

	def get_queryset(self):
		return Period.objects.order_by('system') #'name' changed for 'period_name'

class PeriodCreate(CreateView):
	model = Period
	fields = "__all__"
	template_name = "defcdb/create_period.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PeriodCreate, self).dispatch(*args, **kwargs)


class PeriodUpdate(UpdateView):
	model = Period
	fields = "__all__"
	template_name = 'defcdb/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PeriodUpdate, self).dispatch(*args, **kwargs)


class PeriodDelete(DeleteView):
	model = Period
	template_name = 'defcdb/confirm_delete.html'
	success_url = reverse_lazy('defcdb:period_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PeriodDelete, self).dispatch(*args, **kwargs)


class PeriodDetail(DetailView):
	model = Period
	def get_context_data(self, **kwargs):
		context = super(PeriodDetail, self).get_context_data(**kwargs)
		current_object = self.object
		context['datedby_list'] = current_object.dated_by.all()
		context['datingmethod_list'] = current_object.dating_method.all()
		#context['reference_list'] = current_object.reference.all()
		return context


#################################################################
#				views for Finds									#
#################################################################
class FindsListView(generic.ListView):
	template_name = 'defcdb/finds_list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class. 

	def get_queryset(self):
		return Finds.objects.order_by('finds_type')

@login_required
def update_finds(request, pk):
	instance = get_object_or_404(Finds, id=pk)
	if request.method == "POST":
		form = FindsForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
		return redirect('defcdb:finds_detail', pk=pk)
	else:
		form = FindsForm(instance=instance)
		return render(request, 'defcdb/update_form.html', {'form':form})

@login_required
def create_finds(request):
	if request.method == "POST":
		form = FindsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('defcdb:finds_list')
	else:
		form = FindsForm()
		return render(request, 'defcdb/create_finds.html', {'form':form})



# class FindsCreate(CreateView):
# 	model = Finds
# 	fields = "__all__"
# 	template_name = "defcdb/create_finds.html"

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(FindsCreate, self).dispatch(*args, **kwargs)


# class FindsUpdate(UpdateView):
# 	model = Finds
# 	fields = "__all__"
# 	template_name = 'defcdb/update_form.html'

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(FindsUpdate, self).dispatch(*args, **kwargs)


class FindsDelete(DeleteView):
	model = Finds
	template_name = 'defcdb/confirm_delete.html'
	success_url = reverse_lazy('defcdb:finds_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(FindsDelete, self).dispatch(*args, **kwargs)
class FindsDetail(DetailView):
	model = Finds
	def get_context_data(self, **kwargs):
		context = super(FindsDetail, self).get_context_data(**kwargs)
		current_find = self.object
		context['area_list'] = Area.objects.filter(finds=current_find.id)
		current_find_2 = self.object
		context['interpretation_list'] = Interpretation.objects.filter(finds=current_find_2.id)
		context['smallfindstype_list'] = current_find.small_finds_type.all()
		context['botanyspecies_list'] = current_find.botany_species.all()
		context['animalremainsspecies_list'] = current_find.animal_remains_species.all()
		context['animalremainspart_list'] = current_find.animal_remains_part.all()
		context['lithicsdebitage_list'] = current_find.lithics_debitage.all()
		context['lithicsmodifiedtools_list'] = current_find.lithics_modified_tools.all()
		context['lithicscores_list'] = current_find.lithics_cores.all()
		context['lithicstechnology_list'] = current_find.lithics_technology.all()
		#context['potteryform_list'] = current_find.pottery_form.all()
		context['potterydetail_list'] = current_find.pottery_detail.all()
		context['potterydecoration_list'] = current_find.pottery_decoration.all()
		context['material_list'] = current_find.material.all()
		context['reference_list'] = current_find.reference.all()
		return context


#################################################################
#				views for Site									#
#################################################################
class SiteListView(generic.ListView):
	template_name = 'defcdb/list_list.html'
	# context_object_name = 'object_list' # use object_list instead of
	# # e.g. site_list so the template does not need to be changed so much
	# #for each class. 

	def get_queryset(self):
		return Site.objects.order_by('name')

@login_required
def update_site(request, pk):
	instance = get_object_or_404(Site, id=pk)
	if request.method == "POST":
		form = SiteForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
		#return redirect('../../area/detail/'+pk)
		return redirect('defcdb:site_detail', pk=pk)
	else:
		form = SiteForm(instance=instance)
		return render(request, 'defcdb/update_form.html', {'form':form})

@login_required
def create_site(request):
	if request.method == "POST":
		form = SiteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('defcdb:site_list')
	else:
		form = SiteForm()
		return render(request, 'defcdb/create_site.html', {'form':form})


# class SiteCreate(CreateView):
# 	model = Site
# 	fields = "__all__"
# 	template_name = "defcdb/create_site.html"

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(SiteCreate, self).dispatch(*args, **kwargs)


# class SiteUpdate(UpdateView):
# 	model = Site
# 	fields = "__all__"
# 	template_name = 'defcdb/update_form.html'

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(SiteUpdate, self).dispatch(*args, **kwargs)


class SiteDelete(DeleteView):
	model = Site
	template_name = 'defcdb/confirm_delete.html'
	success_url = reverse_lazy('defcdb:site_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteDelete, self).dispatch(*args, **kwargs)


class SiteDetail(DetailView):
	model = Site
	def get_context_data(self, **kwargs):
		context = super(SiteDetail, self).get_context_data(**kwargs)
		current_site = self.object
		context['areas_list'] = Area.objects.filter(site = current_site.id)
		context['reference_list'] = current_site.reference.all()
		return context

		
#################################################################
#				views for Area									#
#################################################################
class AreaListView(generic.ListView):
	template_name = 'defcdb/area_list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class. 

	def get_queryset(self):
		return Area.objects.order_by('area_type')

@login_required
def update_area(request, pk):
	instance = get_object_or_404(Area, id=pk)
	if request.method == "POST":
		form = AreaForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
		#return redirect('../../area/detail/'+pk)
		return redirect('defcdb:area_detail', pk=pk)
	else:
		form = AreaForm(instance=instance)
		return render(request, 'defcdb/edit_area.html', {'form':form})

@login_required
def create_area(request):
	if request.method == "POST":
		form = AreaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('defcdb:area_list')
	else:
		form = AreaForm()
		return render(request, 'defcdb/create_area.html', {'form':form})


# class AreaCreate(CreateView):
# 	model = Area
# 	fields = "__all__"
# 	template_name = "defcdb/create_area.html"

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(AreaCreate, self).dispatch(*args, **kwargs)


# class AreaUpdate(UpdateView):
# 	model = Area
# 	fields = "__all__"
# 	template_name = 'defcdb/update_form.html'

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(AreaUpdate, self).dispatch(*args, **kwargs)


class AreaDelete(DeleteView):
	model = Area
	template_name = 'defcdb/confirm_delete.html'
	success_url = reverse_lazy('defcdb:area_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AreaDelete, self).dispatch(*args, **kwargs)


class AreaDetail(DetailView):
	model = Area
	def get_context_data(self, **kwargs):
		context = super(AreaDetail, self).get_context_data(**kwargs)
		current_area = self.object
		context['period_reference_list'] = current_area.period_reference.all()
		context['interpretations_list'] = Interpretation.objects.filter(area=current_area.id)
		context['finds_list'] = Finds.objects.filter(area=current_area.id)
		#context['period_list'] = Period.objects.filter(area=current_area.id)
		#context['period_list'] = current_area.period.all()
		context['reference_list'] = current_area.reference.all()
		context['settlementtype_list'] = current_area.settlement_type.all()
		context['settlementstructure_list'] = current_area.settlement_structure.all()
		context['settlementconstructiontype_list'] = current_area.settlement_construction_type.all()
		context['settlementbuildingtechnique_list'] = current_area.settlement_building_technique.all()
		context['settlementspecialfeatures_list'] = current_area.settlement_special_features.all()
		context['evidenceofoccupation_list'] = current_area.cave_rockshelters_evidence_of_occupation.all()
		context['quarryexploitationtype_list'] = current_area.quarry_exploitation_type.all()
		context['quarryrawmaterial_list'] = current_area.quarry_raw_material.all()
		context['topography_list'] = current_area.cemetery_or_graves_topography.all()
		context['mortuaryfeatures_list'] = current_area.cemetery_or_graves_mortuary_features.all()
		context['gravetype_list'] = current_area.grave_type.all()
		context['typeofhumanremains_list'] = current_area.grave_type_of_human_remains.all()
		context['graveagegroups_list'] = current_area.grave_age_groups.all()
		context['gravesexes_list'] = current_area.grave_sexes.all()
		context['manipulationsofgraves_list'] = current_area.grave_manipulations_of_graves.all()
		return context

#################################################################
#				views for Interpretation						#   #to be done
#################################################################
class InterpretationListView(generic.ListView):
	template_name = 'defcdb/interpretation_list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		#return Interpretation.objects.order_by('finds')
		return Interpretation.objects.all()

@login_required
def update_interpretation(request, pk):
	instance = get_object_or_404(Interpretation, id=pk)
	if request.method == "POST":
		form = InterpretationForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
		#return redirect('../../area/detail/'+pk)
		return redirect('defcdb:interpretation_detail', pk=pk)
	else:
		form = InterpretationForm(instance=instance)
		return render(request, 'defcdb/update_form.html', {'form':form})

@login_required
def create_interpretation(request):
	if request.method == "POST":
		form = InterpretationForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('defcdb:interpretation_list')
	else:
		form = InterpretationForm()
		return render(request, 'defcdb/create_interpretation.html', {'form':form})
		
# class InterpretationCreate(CreateView):
# 	model = Interpretation
# 	fields = "__all__"
# 	template_name = "defcdb/create_interpretation.html"

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(InterpretationCreate, self).dispatch(*args, **kwargs)


# class InterpretationUpdate(UpdateView):
# 	model = Interpretation
# 	fields = "__all__"
# 	template_name = 'defcdb/update_form.html'

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(InterpretationUpdate, self).dispatch(*args, **kwargs)

class InterpretationDelete(DeleteView):
	model = Interpretation
	template_name = 'defcdb/confirm_delete.html'
	success_url = reverse_lazy('defcdb:interpretation_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(InterpretationDelete, self).dispatch(*args, **kwargs)

class InterpretationDetail(DetailView):
	model = Interpretation
	def get_context_data(self, **kwargs):
		context = super(InterpretationDetail, self).get_context_data(**kwargs)
		#current_interpretation = self.object
		#context = ['finds_list'] = Finds.objects.filter(interpretation=current_interpretation.id) 
		#instead we are using ManytoMany so all finds will be in finds field
		current_object = self.object
		context['areas_list'] = current_object.area.all()
		context['finds_list'] = current_object.finds.all()
		context['productiontype_list'] = current_object.production_type.all()
		context['subsistencetype_list'] = current_object.subsistence_type.all()
		context['reference_list'] = current_object.reference.all()
		return context

#################################################################
#				views for login/logout							#
#################################################################
def user_login(request):
	errors=[]
	if request.method == 'POST':
		form = form_user_login(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(request.GET.get('next','/defcdb/'))
				else:
					return HttpResponse('not active.')
			else:
				return HttpResponse('user does not exist')
	else:
		form = form_user_login()
		return render(request, 'defcdb/user_login.html', {'form':form})


def user_logout(request):
	logout(request)
	return render_to_response('defcdb/logout.html')

#################################################################
#				basic application views							#
#################################################################


def start_view(request):
	context = RequestContext(request)
	return render(request, 'defcdb/index.html', context)

