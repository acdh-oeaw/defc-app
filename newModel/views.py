# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse, reverse_lazy

from .models import Site, Area, Finds, Period, ResearchEvent, Interpretation, DC_period_datingmethod, DC_researchevent_researchtype
from .forms import form_user_login


#################################################################
#				views for ResearchEvent							#
#################################################################
class ResearchEventListView(generic.ListView):
	template_name = 'newModel/researchEvent_list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		return ResearchEvent.objects.order_by('id')


class ResearchEventCreate(CreateView):
	model = ResearchEvent
	fields = "__all__"
	template_name = "newModel/create_researchevent.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ResearchEventCreate, self).dispatch(*args, **kwargs)


class ResearchEventUpdate(UpdateView):
	model = ResearchEvent
	fields = "__all__"
	template_name = 'newModel/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ResearchEventUpdate, self).dispatch(*args, **kwargs)


class ResearchEventDelete(DeleteView):
	model = ResearchEvent
	template_name = 'newModel/confirm_delete.html'
	success_url = reverse_lazy('newModel:researchevent_list')

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
	template_name = 'newModel/list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class.

	def get_queryset(self):
		return Period.objects.order_by('system') #'name' changed for 'period_name'

class PeriodCreate(CreateView):
	model = Period
	fields = "__all__"
	template_name = "newModel/create_period.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PeriodCreate, self).dispatch(*args, **kwargs)


class PeriodUpdate(UpdateView):
	model = Period
	fields = "__all__"
	template_name = 'newModel/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PeriodUpdate, self).dispatch(*args, **kwargs)


class PeriodDelete(DeleteView):
	model = Period
	template_name = 'newModel/confirm_delete.html'
	success_url = reverse_lazy('newModel:period_list')

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
		context['reference_list'] = current_object.reference.all()
		return context


#################################################################
#				views for Finds									#
#################################################################
class FindsListView(generic.ListView):
	template_name = 'newModel/list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class. 

	def get_queryset(self):
		return Finds.objects.order_by('finds_type') 


class FindsCreate(CreateView):
	model = Finds
	fields = "__all__"
	template_name = "newModel/create_finds.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(FindsCreate, self).dispatch(*args, **kwargs)


class FindsUpdate(UpdateView):
	model = Finds
	fields = "__all__"
	template_name = 'newModel/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(FindsUpdate, self).dispatch(*args, **kwargs)


class FindsDelete(DeleteView):
	model = Finds
	template_name = 'newModel/confirm_delete.html'
	success_url = reverse_lazy('newModel:finds_list')

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
		context['potteryform_list'] = current_find.pottery_form.all()
		context['potterydetail_list'] = current_find.pottery_detail.all()
		context['potterydecoration_list'] = current_find.pottery_decoration.all()
		context['material_list'] = current_find.material.all()
		context['reference_list'] = current_find.reference.all()
		return context


#################################################################
#				views for Site									#
#################################################################
class SiteListView(generic.ListView):
	template_name = 'newModel/site_list.html'

	def get_queryset(self):
		return Site.objects.order_by('name')


class SiteCreate(CreateView):
	model = Site
	fields = "__all__"
	template_name = "newModel/create_site.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteCreate, self).dispatch(*args, **kwargs)


class SiteUpdate(UpdateView):
	model = Site
	fields = "__all__"
	template_name = 'newModel/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteUpdate, self).dispatch(*args, **kwargs)


class SiteDelete(DeleteView):
	model = Site
	template_name = 'newModel/confirm_delete.html'
	success_url = reverse_lazy('newModel:site_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteDelete, self).dispatch(*args, **kwargs)


class SiteDetail(DetailView):
	model = Site
	def get_context_data(self, **kwargs):
		context = super(SiteDetail, self).get_context_data(**kwargs)
		current_site = self.object
		context['areas_list'] = Area.objects.filter(site = current_site.id)
		context['reference_list'] = current_site.reference_site.all()
		return context

		
#################################################################
#				views for Area									#
#################################################################
class AreaListView(generic.ListView):
	template_name = 'newModel/list.html'
	context_object_name = 'object_list' # use object_list instead of
	# e.g. site_list so the template does not need to be changed so much
	#for each class. 

	def get_queryset(self):
		return Area.objects.order_by('area_type')


class AreaCreate(CreateView):
	model = Area
	fields = "__all__"
	template_name = "newModel/create_area.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AreaCreate, self).dispatch(*args, **kwargs)


class AreaUpdate(UpdateView):
	model = Area
	fields = "__all__"
	template_name = 'newModel/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AreaUpdate, self).dispatch(*args, **kwargs)


class AreaDelete(DeleteView):
	model = Area
	template_name = 'newModel/confirm_delete.html'
	success_url = reverse_lazy('newModel:area_list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AreaDelete, self).dispatch(*args, **kwargs)


class AreaDetail(DetailView):
	model = Area
	def get_context_data(self, **kwargs):
		context = super(AreaDetail, self).get_context_data(**kwargs)
		current_area = self.object
		context['interpretations_list'] = Interpretation.objects.filter(area=current_area.id)
		context['finds_list'] = Finds.objects.filter(area=current_area.id)
		#context['period_list'] = Period.objects.filter(area=current_area.id)
		context['period_list'] = current_area.period.all()
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
	template_name = 'newModel/list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		#return Interpretation.objects.order_by('finds')
		return Interpretation.objects.all()
		
class InterpretationCreate(CreateView):
	model = Interpretation
	fields = "__all__"
	template_name = "newModel/create_interpretation.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(InterpretationCreate, self).dispatch(*args, **kwargs)


class InterpretationUpdate(UpdateView):
	model = Interpretation
	fields = "__all__"
	template_name = 'newModel/update_form.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(InterpretationUpdate, self).dispatch(*args, **kwargs)

class InterpretationDelete(DeleteView):
	model = Interpretation
	template_name = 'newModel/confirm_delete.html'
	success_url = reverse_lazy('newModel:interpretation_list')

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
					return HttpResponseRedirect(request.GET.get('next','/newModel/'))
				else:
					return HttpResponse('not active.')
			else:
				return HttpResponse('user does not exist')
	else:
		form = form_user_login()
		return render(request, 'newModel/user_login.html', {'form':form})


def user_logout(request):
	logout(request)
	return render_to_response('newModel/logout.html')

#################################################################
#				basic application views							#
#################################################################


def start_view(request):
	context = RequestContext(request)
	return render(request, 'newModel/index.html', context)

