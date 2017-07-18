from django_tables2 import SingleTableView, RequestConfig
from defcdb.models import (
    Site, Area, Finds, DC_chronological_system, ResearchEvent,
    DC_researchevent_institution)
from defcdb.models import Interpretation
from .filters import (
    SiteListFilter, AreaListFilter, FindsListFilter, ResearchEventListFilter,
    InterpretationListFilter)
from .forms import GenericFilterFormHelper, SpecificAreaForm, SpecificFindsForm
from .tables import SiteTable, AreaTable, FindsTable, ResearchEventTable, InterpretationTable
import csv
import re
import time
import datetime
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


def serialize(modelclass):
    fields = modelclass._meta.get_fields(include_parents=False)
    serialized = []
    for field in fields:
        if field.auto_created is True:
            pass
        elif field.get_internal_type() == "ManyToManyField":
            attrs = getattr(modelclass, field.name)
            values = "|".join([str(y[1]) for y in attrs.values_list()])
            key_value = values
            serialized.append(key_value)
        elif field.get_internal_type() == "ForeignKey":
            if getattr(modelclass, field.name) is not None:
                key_value = getattr(modelclass, field.name)
                serialized.append(key_value)
            else:
                key_value = 'not defined'
                serialized.append(key_value)
        else:
            key_value = getattr(modelclass, field.name)
            serialized.append(key_value)
    return serialized


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class SiteDownloadView(GenericListView):
    model = Site
    table_class = SiteTable
    template_name = 'browsing/site_list_generic.html'
    filter_class = SiteListFilter
    formhelper_class = GenericFilterFormHelper

    def render_to_response(self, context, **kwargs):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='text/csv')
        filename = "defc_sites_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(filename)
        writer = csv.writer(response, delimiter=",")
        writer.writerow([
            'Site ID', 'Name of the site',
            'Alias name', 'Alternative name',
            'District', 'Region', 'Country',
            'Geographical Coordinate Reference System', 'Coordinate source',
            'Latitude', 'Longitude', 'Elevation',
            'Authority file ID (Geonames ID)',
            'Topography', 'Description',
            'Exact location',
            'Number of activity periods',
            'Reference', 'Comment']
        )
        for obj in self.get_queryset():
            if obj.province and obj.province.region:
                writer.writerow([obj.id, obj.name, '; '.join([obj.name for obj in obj.alias_name.all()]),
                                '; '.join([obj.name for obj in obj.alternative_name.all()]),
                                obj.province.name, obj.province.region.name, obj.province.region.country.name,
                                obj.geographical_coordinate_reference_system,
                                obj.coordinate_source, obj.latitude, obj.longitude,
                                obj.elevation, obj.authorityfile_id, obj.topography,
                                obj.description, obj.exact_location, obj.number_of_activity_periods,
                                '; '.join([obj.author +' '+ obj.title+' '+ str(obj.publication_year) +' '+ str(obj.place) for obj in obj.reference.all()]),
                                obj.comment])
            else:
                writer.writerow([obj.id, obj.name, '; '.join([obj.name for obj in obj.alias_name.all()]),
                                '; '.join([obj.name for obj in obj.alternative_name.all()]),
                                obj.province, 'not defined', 'not defined',
                                obj.geographical_coordinate_reference_system,
                                obj.coordinate_source, obj.latitude, obj.longitude,
                                obj.elevation, obj.authorityfile_id, obj.topography,
                                obj.description, obj.exact_location, obj.number_of_activity_periods,
                                # '; '.join([obj.author +' '+ obj.title+' '+ str(obj.publication_year) +' '+ str(obj.place) for obj in obj.reference.all()]),
                                '; '.join([str(obj) for obj in obj.reference.all()]),
                                obj.comment])

        return response


class SiteListView(GenericListView):
    model = Site
    table_class = SiteTable
    template_name = 'browsing/site_list_generic.html'
    filter_class = SiteListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        site_names = []
        for x in Site.objects.all():
            site_names.append(x.name)
        context["site_names"] = set(site_names)
        cs_names = []
        period_names = []
        for x in DC_chronological_system.objects.all():
            cs_names.append(x.cs_name)
            period_names.append(x.period_name)
        context["cs_names"] = set(cs_names)
        context["period_names"] = set(period_names)
        return context


def download_results(request):
    # queryset = Site.objects.filter(name__icontains='los')

    f = SiteListFilter(request.GET, queryset=Site.objects.all())
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
    response = HttpResponse(content_type='text/csv')
    filename = "defc_sites_{}".format(timestamp)
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(filename)
    writer = csv.writer(response, delimiter=",")
    writer.writerow([
        'Site ID', 'Name of the site',
        'Alias name', 'Alternative name',
        'District', 'Region', 'Country',
        'Geographical Coordinate Reference System', 'Coordinate source',
        'Latitude', 'Longitude', 'Elevation',
        'Authority file ID (Geonames ID)',
        'Topography', 'Description',
        'Exact location',
        'Number of activity periods',
        'Reference', 'Comment']
    )
    for obj in f.qs.values():
        if obj.province and obj.province.region:
            writer.writerow([obj.id, obj.name, '; '.join([obj.name for obj in obj.alias_name.all()]),
                            '; '.join([obj.name for obj in obj.alternative_name.all()]),
                            obj.province.name, obj.province.region.name, obj.province.region.country.name,
                            obj.geographical_coordinate_reference_system,
                            obj.coordinate_source, obj.latitude, obj.longitude,
                            obj.elevation, obj.authorityfile_id, obj.topography,
                            obj.description, obj.exact_location, obj.number_of_activity_periods,
                            '; '.join([obj.author +' '+ obj.title+' '+ str(obj.publication_year) +' '+ str(obj.place) for obj in obj.reference.all()]),
                            obj.comment])
        else:
            writer.writerow([obj.id, obj.name, '; '.join([obj.name for obj in obj.alias_name.all()]),
                            '; '.join([obj.name for obj in obj.alternative_name.all()]),
                            obj.province, 'not defined', 'not defined',
                            obj.geographical_coordinate_reference_system,
                            obj.coordinate_source, obj.latitude, obj.longitude,
                            obj.elevation, obj.authorityfile_id, obj.topography,
                            obj.description, obj.exact_location, obj.number_of_activity_periods,
                            '; '.join([obj.author +' '+ obj.title+' '+ str(obj.publication_year) +' '+ str(obj.place) for obj in obj.reference.all()]),
                            obj.comment])

    return response


class AreaDownloadView(GenericListView):
    model = Area
    table_class = AreaTable
    template_name = 'browsing/area_list_generic.html'
    filter_class = AreaListFilter
    formhelper_class = GenericFilterFormHelper

    def render_to_response(self, context, **kwargs):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='text/csv')
        filename = "defc_areas_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(filename)
        writer = csv.writer(response, delimiter=",")
        writer.writerow([
            'Area ID', 'Name of the site',
            'area_type', 'area_nr',
            'period', 'dating_method', 'radiocarbon_dated',
            'earliest_date_14C_age',
            'earliest_date_standard_deviation',
            'earliest_datedated_by',
            'latest_date_14C_age',
            'latest_date_standard_deviation',
            'latest_datedated_by',
            'period_reference', 'period_comment',
            'settlement_type', 'settlement_structure',
            'settlement_construction_type', 'settlement_construction_shape',
            'settlement_building_technique',
            'settlement_special_features',
            'settlement_human_remains',
            'cave_rockshelters_type',
            'cave_rockshelters_human_remains',
            'cave_rockshelters_evidence_of_occupation',
            'quarry_exploitation_type',
            'quarry_raw_material',
            'cemetery_or_grave',
            'cemetery_or_graves_topography',
            'cemetery_or_graves_mortuary_features',
            'grave_number_of_graves',
            'grave_type', 'grave_type_of_human_remains',
            'grave_estimated_number_of_individuals',
            'grave_age_groups', 'grave_sexes', 'grave_number_of_female_sex',
            'grave_number_of_male_sex', 'grave_number_of_not_specified_sex',
            'grave_manipulations_of_graves', 'description', 'reference',
            'comment'
#43 fields
             ]
        )
        for obj in self.get_queryset():
            writer.writerow([obj.id, obj.site.name, obj.area_type,
                            obj.area_nr,
                            '; '.join([str(obj) for obj in obj.period.all()]),
                            '; '.join([str(obj) for obj in obj.dating_method.all()]),
                            obj.radiocarbon_dated,
                            obj.earliest_date_14C_age,
                            obj.earliest_date_standard_deviation,
                            '; '.join([str(obj) for obj in obj.earliest_datedated_by.all()]),
                            obj.latest_date_14C_age,
                            obj.latest_date_standard_deviation,
                            '; '.join([str(obj) for obj in obj.latest_datedated_by.all()]),

                            '; '.join([str(obj) for obj in obj.period_reference.all()]),
                            obj.period_comment,
                            obj.settlement_type,
                            '; '.join([str(obj) for obj in obj.settlement_structure.all()]),
                            '; '.join([str(obj) for obj in obj.settlement_construction_type.all()]),
                            '; '.join([str(obj) for obj in obj.settlement_construction_shape.all()]),
                            '; '.join([str(obj) for obj in obj.settlement_building_technique.all()]),
                            '; '.join([str(obj) for obj in obj.settlement_special_features.all()]),
                            obj.settlement_human_remains,
                            obj.cave_rockshelters_type,
                            obj.cave_rockshelters_human_remains,
                            '; '.join([str(obj) for obj in obj.cave_rockshelters_evidence_of_occupation.all()]),
                            obj.quarry_exploitation_type,
                            '; '.join([str(obj) for obj in obj.quarry_raw_material.all()]),
                            obj.cemetery_or_grave,
                            '; '.join([str(obj) for obj in obj.cemetery_or_graves_topography.all()]),
                            '; '.join([str(obj) for obj in obj.cemetery_or_graves_mortuary_features.all()]),
                            obj.grave_number_of_graves,
                            '; '.join([str(obj) for obj in obj.grave_type.all()]),

                            '; '.join([str(obj) for obj in obj.grave_type_of_human_remains.all()]),
                            obj.grave_estimated_number_of_individuals,
                            '; '.join([str(obj) for obj in obj.grave_age_groups.all()]),
                            '; '.join([str(obj) for obj in obj.grave_sexes.all()]),
                            obj.grave_number_of_female_sex, obj.grave_number_of_male_sex,
                            obj.grave_number_of_not_specified_sex,
                            '; '.join([str(obj) for obj in obj.grave_manipulations_of_graves.all()]),
                            obj.description,
                            '; '.join([str(obj) for obj in obj.reference.all()]),
                            obj.comment])
        return response


class AreaListView(GenericListView):
    model = Area
    table_class = AreaTable
    template_name = 'browsing/area_list_generic.html'
    filter_class = AreaListFilter
    formhelper_class = SpecificAreaForm

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        site_names = []
        for x in Site.objects.all():
            site_names.append(x.name)
        context["site_names"] = set(site_names)
        cs_names = []
        period_names = []
        for x in DC_chronological_system.objects.all():
            cs_names.append(x.cs_name)
            period_names.append(x.period_name)
        context["cs_names"] = set(cs_names)
        context["period_names"] = set(period_names)
        return context


class FindsDownloadView(GenericListView):
    model = Finds
    table_class = FindsTable
    template_name = 'browsing/finds_list_generic.html'
    filter_class = FindsListFilter
    formhelper_class = GenericFilterFormHelper

    def render_to_response(self, context, **kwargs):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='text/csv')
        filename = "defc_finds_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(filename)
        writer = csv.writer(response, delimiter=",")
        writer.writerow([
            'Finds ID', 'Area',
            'research_event',
            'finds_type',
            'small_finds_category',
            'small_finds_type',
            'botany_species',
            'animal_remains_species',
            'animal_remains_completeness',
            'animal_remains_part',
            'lithics_technology',
            'lithics_industry',
            'lithics_core_shape',
            'lithics_retouched_tools',
            'lithics_unretouched_tools',
            'lithics_raw_material',
            'obsidian',
            'obsidian_amount',
            'pottery_form',
            'pottery_detail',
            'pottery_decoration',
            'pottery_type',
            'amount',
            'material',
            'confidence',
            'reference',
            'comment',
            #27
             ]
        )
        for obj in self.get_queryset():
            writer.writerow([obj.id,
                            obj.area,
                            obj.research_event,
                            obj.finds_type,
                            obj.small_finds_category,
                            '; '.join([str(obj) for obj in obj.small_finds_type.all()]),
                            '; '.join([str(obj) for obj in obj.botany_species.all()]),
                            '; '.join([str(obj) for obj in obj.animal_remains_species.all()]),
                            obj.animal_remains_completeness,
                            '; '.join([str(obj) for obj in obj.animal_remains_part.all()]),
                            '; '.join([str(obj) for obj in obj.lithics_technology.all()]),
                            '; '.join([str(obj) for obj in obj.lithics_industry.all()]),
                            '; '.join([str(obj) for obj in obj.lithics_core_shape.all()]),
                            '; '.join([str(obj) for obj in obj.lithics_retouched_tools.all()]),
                            '; '.join([str(obj) for obj in obj.lithics_unretouched_tools.all()]),
                            '; '.join([str(obj) for obj in obj.lithics_raw_material.all()]),
                            obj.obsidian,
                            obj.obsidian_amount,
                            obj.pottery_form,
                            '; '.join([str(obj) for obj in obj.pottery_detail.all()]),
                            '; '.join([str(obj) for obj in obj.pottery_decoration.all()]),
                            obj.pottery_type,
                            obj.amount,
                            '; '.join([str(obj) for obj in obj.material.all()]),
                            obj.confidence,
                            '; '.join([str(obj) for obj in obj.reference.all()]),
                            obj.comment])
        return response
#27


class FindsListView(GenericListView):
    model = Finds
    table_class = FindsTable
    template_name = 'browsing/finds_list_generic.html'
    filter_class = FindsListFilter
    formhelper_class = SpecificFindsForm

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        site_names = []
        for x in Site.objects.all():
            site_names.append(x.name)
        context["site_names"] = set(site_names)
        cs_names = []
        period_names = []
        for x in DC_chronological_system.objects.all():
            cs_names.append(x.cs_name)
            period_names.append(x.period_name)
        context["cs_names"] = set(cs_names)
        context["period_names"] = set(period_names)
        return context


class ResearchEventListView(GenericListView):
    model = ResearchEvent
    table_class = ResearchEventTable
    template_name = 'browsing/researchevent_list_generic.html'
    filter_class = ResearchEventListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        institution_names = []
        for x in DC_researchevent_institution.objects.all():
            institution_names.append(x.name)
        context["institution_names"] = set(institution_names)
        project_names = []
        for x in ResearchEvent.objects.all():
            project_names.append(x.project_name)
        context["project_names"] = set(project_names)
        site_names = []
        for x in Site.objects.all():
            site_names.append(x.name)
        context["site_names"] = set(site_names)
        return context


class InterpretationListView(GenericListView):
    model = Interpretation
    table_class = InterpretationTable
    template_name = 'browsing/interpretation_list_generic.html'
    filter_class = InterpretationListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        site_names = []
        for x in Site.objects.all():
            site_names.append(x.name)
        context["site_names"] = set(site_names)
        return context
