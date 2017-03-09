# -*- coding: utf-8 -*-
from django.views import generic
from django.views.generic.detail import DetailView
from threedmodels.models import *
from defcdb.models import Site, Area, ResearchEvent, Finds, Interpretation
from images_metadata.models import ImageThesaurus

#################################################################
#               views for ResearchEvent                         #
#################################################################


class ResearchEventListView(generic.ListView):
    model = ResearchEvent
    template_name = 'publicrecords/public_researchevent_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return ResearchEvent.objects.filter(public=True).order_by('id')


class ResearchEventDetail(DetailView):
    template_name = 'publicrecords/public_researchevent_detail.html'
    model = ResearchEvent

    def get_context_data(self, **kwargs):
        context = super(ResearchEventDetail, self).get_context_data(**kwargs)
        current_object = self.object
        context['researchtype_list'] = current_object.research_type.all()
        context['institution_list'] = current_object.institution.all()
        context['specialanalysis_list'] = current_object.special_analysis.all()
        context['reference_list'] = current_object.reference.all()
        context['finds_list'] = Finds.objects.filter(research_event=current_object.id)
        return context


#################################################################
#               views for Finds                                 #
#################################################################


class FindsListView(generic.ListView):
    template_name = 'publicrecords/public_finds_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Finds.objects.filter(public=True).order_by('finds_type')


class FindsDetail(DetailView):
    template_name = 'publicrecords/public_finds_detail.html'
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
        context['lithicsunretouchedtools_list'] = current_find.lithics_unretouched_tools.all()
        context['lithicsrawmaterial_list'] = current_find.lithics_raw_material.all()
        context['potterydetail_list'] = current_find.pottery_detail.all()
        context['potterydecoration_list'] = current_find.pottery_decoration.all()
        context['material_list'] = current_find.material.all()
        context['reference_list'] = current_find.reference.all()
        context['threedmodel'] = Threedmodel.objects.filter(finds=current_find.id)
        if current_find.pottery_form is not None:
            context['pottery_form_list'] = ImageThesaurus.objects.filter(
                pottery_form=current_find.pottery_form)
        if current_find.pottery_detail is not None:
            context['pottery_detail_list'] = ImageThesaurus.objects.filter(
                pottery_detail=current_find.pottery_detail.all)
        if current_find.pottery_decoration is not None:
            context['pottery_decoration_list'] = ImageThesaurus.objects.filter(
                pottery_decoration=current_find.pottery_decoration.all)
        return context


#################################################################
#               views for Site                                  #
#################################################################


class SiteListView(generic.ListView):
    template_name = 'publicrecords/public_site_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Site.objects.filter(public=True).order_by('name')


class SiteDetail(DetailView):
    template_name = 'publicrecords/public_site_detail.html'
    model = Site

    def get_context_data(self, **kwargs):
        context = super(SiteDetail, self).get_context_data(**kwargs)
        current_site = self.object
        context['areas_list'] = Area.objects.filter(site=current_site.id)
        context['reference_list'] = current_site.reference.all()
        context['aliasName_list'] = current_site.alias_name.all()
        context['alternativeName_list'] = current_site.alternative_name.all()
        return context

#################################################################
#               views for Area                                  #
#################################################################


class AreaListView(generic.ListView):
    template_name = 'publicrecords/public_area_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Area.objects.filter(public=True).order_by('area_type')


class AreaDetail(DetailView):
    template_name = 'publicrecords/public_area_detail.html'
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
        context['settlementconstructionshape_list'] = current_area.settlement_construction_shape.all()
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
#               views for Interpretation                        #
#################################################################


class InterpretationListView(generic.ListView):
    template_name = 'publicrecords/public_interpretation_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Interpretation.objects.filter(public=True).order_by('id')


class InterpretationDetail(DetailView):
    template_name = 'publicrecords/public_interpretation_detail.html'
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
