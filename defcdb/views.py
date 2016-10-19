# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from reversion import revisions as reversion
from haystack.query import SearchQuerySet

from .models import Site, Area, Finds, ResearchEvent, Interpretation
from .forms import (
    NameForm, form_user_login, AreaForm, ResearcheventForm, FindsForm, SiteForm, InterpretationForm
)
from .serializers import *


#################################################################
#               views for ResearchEvent                         #
#################################################################

def search_all(request):
    context = {}
    if 'q' in request.GET:
        searchstring = request.GET.get('q', '')
        results = SearchQuerySet().filter(content=searchstring).load_all()
        total_results = results.count()
    else:
        searchstring = None
        total_results = None
        results = None
    context['searchstring'] = searchstring
    context['total_results'] = total_results
    context['results'] = results
    return render(request, 'defcdb/search_all.html', context)


class ResearchEventListView(generic.ListView):
    model = ResearchEvent
    template_name = 'defcdb/researchevent_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return ResearchEvent.objects.order_by('id')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResearchEventListView, self).dispatch(*args, **kwargs)


@login_required
def update_researchevent(request, pk):
    instance = get_object_or_404(ResearchEvent, id=pk)
    if request.method == "POST":
        form = ResearcheventForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('publicrecords:researchevent_detail', pk=pk)
    else:
        form = ResearcheventForm(instance=instance)
        return render(
            request, 'defcdb/update_form.html', {'form': form, 'classname': "research event"}
        )


@login_required
def create_researchevent(request):
    if request.method == "POST":
        form = ResearcheventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browsing:browse_researchevents')
        else:
            return render(request, 'defcdb/create_researchevent.html', {'form': form})
    else:
        form = ResearcheventForm()
        return render(request, 'defcdb/create_researchevent.html', {'form': form})


class ResearchEventDelete(DeleteView):
    model = ResearchEvent
    template_name = 'defcdb/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_researchevents')

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResearchEventDetail, self).dispatch(*args, **kwargs)


#################################################################
#               views for Finds                                 #
#################################################################
class FindsListView(generic.ListView):
    template_name = 'defcdb/finds_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Finds.objects.order_by('finds_type')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FindsListView, self).dispatch(*args, **kwargs)


@login_required
def update_finds(request, pk):
    instance = get_object_or_404(Finds, id=pk)
    if request.method == "POST":
        form = FindsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('publicrecords:finds_detail', pk=pk)
    else:
        form = FindsForm(instance=instance)
        return render(
            request, 'defcdb/edit_finds.html', {'form': form, 'classname': "finds"})


@login_required
def create_finds(request):
    if request.method == "POST":
        form = FindsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browsing:browse_finds')
        else:
            return render(request, 'defcdb/create_finds.html', {'form': form})
    else:
        form = FindsForm()
        return render(request, 'defcdb/create_finds.html', {'form': form})


class FindsDelete(DeleteView):
    model = Finds
    template_name = 'defcdb/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_finds')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FindsDelete, self).dispatch(*args, **kwargs)


class FindsDetail(DetailView):
    model = Finds

    def get_context_data(self, **kwargs):
        context = super(FindsDetail, self).get_context_data(**kwargs)
        current_find = self.object
        context['area_list'] = Area.objects.filter(finds=current_find.id)
        context['researchevent_list'] = ResearchEvent.objects.filter(finds=current_find.id)
        current_find_2 = self.object
        context['interpretation_list'] = Interpretation.objects.filter(finds=current_find_2.id)
        context['smallfindstype_list'] = current_find.small_finds_type.all()
        context['botanyspecies_list'] = current_find.botany_species.all()
        context['animalremainsspecies_list'] = current_find.animal_remains_species.all()
        context['animalremainspart_list'] = current_find.animal_remains_part.all()
        context['lithicstechnology_list'] = current_find.lithics_technology.all()
        context['lithicsindustry_list'] = current_find.lithics_industry.all()
        context['lithicscoreshape_list'] = current_find.lithics_core_shape.all()
        context['lithicsretouchedtools_list'] = current_find.lithics_retouched_tools.all()
        context['lithicsrawmaterial_list'] = current_find.lithics_raw_material.all()
        context['potterydetail_list'] = current_find.pottery_detail.all()
        context['potterydecoration_list'] = current_find.pottery_decoration.all()
        context['material_list'] = current_find.material.all()
        context['reference_list'] = current_find.reference.all()
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FindsDetail, self).dispatch(*args, **kwargs)


#################################################################
#               views for Name                              #
#################################################################
@login_required
def create_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("""<html><body><h1>saved</h1>
                <script type="text/javascript">
                    function closeWindow() {
                        setTimeout(function() {
                        window.close();
                        }, 1000);
                        }
                        window.onload = closeWindow();
                </script></body></html>""")
    else:
        form = NameForm()
        return render(request, 'defcdb/create_name.html', {'form': form})


#################################################################
#               views for Site                                  #
#################################################################

class SiteListView(generic.ListView):
    template_name = 'defcdb/site_list.html'

    def get_queryset(self):
        return Site.objects.order_by('name')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SiteListView, self).dispatch(*args, **kwargs)


@reversion.create_revision()
@login_required
def update_site(request, pk):
    instance = get_object_or_404(Site, id=pk)
    if request.method == "POST":
        form = SiteForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('publicrecords:site_detail', pk=pk)
    else:
        form = SiteForm(instance=instance)
        return render(request, 'defcdb/update_form.html', {'form': form, 'classname': "site"})


@login_required
@reversion.create_revision()
def create_site(request):
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browsing:browse_sites')
        else:
            return render(request, 'defcdb/create_site.html', {'form': form})
    else:
        form = SiteForm()
        return render(request, 'defcdb/create_site.html', {'form': form})


class SiteDelete(DeleteView):
    model = Site
    template_name = 'defcdb/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_sites')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SiteDelete, self).dispatch(*args, **kwargs)


class SiteDetail(DetailView):
    model = Site

    def get_context_data(self, **kwargs):
        context = super(SiteDetail, self).get_context_data(**kwargs)
        current_site = self.object
        context['areas_list'] = Area.objects.filter(site=current_site.id)
        context['reference_list'] = current_site.reference.all()
        context['aliasName_list'] = current_site.alias_name.all()
        context['alternativeName_list'] = current_site.alternative_name.all()
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SiteDetail, self).dispatch(*args, **kwargs)


#################################################################
#               views for Area                                  #
#################################################################
class AreaListView(generic.ListView):
    template_name = 'defcdb/area_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Area.objects.order_by('area_type')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AreaListView, self).dispatch(*args, **kwargs)


@reversion.create_revision()
@login_required
def update_area(request, pk):
    instance = get_object_or_404(Area, id=pk)
    if request.method == "POST":
        form = AreaForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('publicrecords:area_detail', pk=pk)
    else:
        form = AreaForm(instance=instance)
        return render(request, 'defcdb/edit_area.html', {'form': form, 'classname': "area"})


@reversion.create_revision()
@login_required
def create_area(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browsing:browse_areas')
        else:
            return render(request, 'defcdb/create_area.html', {'form': form})
    else:
        form = AreaForm()
        return render(request, 'defcdb/create_area.html', {'form': form})


class AreaDelete(DeleteView):
    model = Area
    template_name = 'defcdb/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_areas')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AreaDelete, self).dispatch(*args, **kwargs)


class AreaDetail(DetailView):
    model = Area

    def get_context_data(self, **kwargs):
        context = super(AreaDetail, self).get_context_data(**kwargs)
        current_area = self.object
        context['sites_list'] = Site.objects.filter(area=current_area.id)
        context['period_reference_list'] = current_area.period_reference.all()
        context['period_list'] = current_area.period.all()
        context['dating_method_list'] = current_area.dating_method.all()
        context['datedby_list'] = current_area.earliest_datedated_by.all()
        context['datedby_list'] = current_area.latest_datedated_by.all()
        context['interpretations_list'] = Interpretation.objects.filter(area=current_area.id)
        context['finds_list'] = Finds.objects.filter(area=current_area.id)
        context['reference_list'] = current_area.reference.all()
        context['settlementstructure_list'] = current_area.settlement_structure.all()
        context['settlementconstructiontype_list'] = current_area.settlement_construction_type.all()
        context['settlementbuildingtechnique_list'] = current_area.settlement_building_technique.all()
        context['settlementspecialfeatures_list'] = current_area.settlement_special_features.all()
        context['evidenceofoccupation_list'] = current_area.cave_rockshelters_evidence_of_occupation.all()
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
#               views for Interpretation                        #   #to be done
#################################################################
class InterpretationListView(generic.ListView):
    template_name = 'defcdb/interpretation_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Interpretation.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InterpretationListView, self).dispatch(*args, **kwargs)


@reversion.create_revision()
@login_required
def update_interpretation(request, pk):
    instance = get_object_or_404(Interpretation, id=pk)
    if request.method == "POST":
        form = InterpretationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('publicrecords:interpretation_detail', pk=pk)
    else:
        form = InterpretationForm(instance=instance)
        return render(
            request, 'defcdb/update_form.html', {'form': form, 'classname': "interpretation"}
        )


@reversion.create_revision()
@login_required
def create_interpretation(request):
    if request.method == "POST":
        form = InterpretationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browsing:browse_interpretations')
        else:
            return render(request, 'defcdb/create_interpretation.html', {'form': form})
    else:
        form = InterpretationForm()
        return render(request, 'defcdb/create_interpretation.html', {'form': form})


class InterpretationDelete(DeleteView):
    model = Interpretation
    template_name = 'defcdb/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_interpretations')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InterpretationDelete, self).dispatch(*args, **kwargs)


class InterpretationDetail(DetailView):
    model = Interpretation

    def get_context_data(self, **kwargs):
        context = super(InterpretationDetail, self).get_context_data(**kwargs)
        current_object = self.object
        context['areas_list'] = current_object.area.all()
        context['finds_list'] = current_object.finds.all()
        context['productiontype_list'] = current_object.production_type.all()
        context['subsistencetype_list'] = current_object.subsistence_type.all()
        context['reference_list'] = current_object.reference.all()
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InterpretationDetail, self).dispatch(*args, **kwargs)

#################################################################
#               views for login/logout                          #
#################################################################


def user_login(request):
    if request.method == 'POST':
        form = form_user_login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get('next', '/'))
                else:
                    return HttpResponse('not active.')
            else:
                return HttpResponse('user does not exist')
    else:
        form = form_user_login()
        return render(request, 'defcdb/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render_to_response('defcdb/logout.html')

#################################################################
#               basic application views                         #
#################################################################


def start_view(request):
    context = RequestContext(request)
    return render(request, 'webpage/index.html', context)


def turkey_map_view(request):
    return render(request, 'defcdb/turkey_map.html')


def greece_map_view(request):
    return render(request, 'defcdb/greece_map.html')


def bibliography_view(request):
    return render(request, 'defcdb/bibliography.html')
