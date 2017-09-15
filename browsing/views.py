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
            'Area type', 'Area nr',
            'Period', 'Dating method', 'Radiocarbon dated',
            'Earliest date 14C age',
            'Earliest date standard deviation',
            'Earliest datedated by',
            'Latest date 14C age',
            'Latest date standard deviation',
            'Latest datedated by',
            'Period reference', 'Period comment',
            'Settlement type', 'Settlement structure',
            'Settlement construction type', 'Settlement construction shape',
            'Settlement building technique',
            'Settlement special features',
            'Settlement human remains',
            'Cave rockshelters type',
            'Cave rockshelters human remains',
            'Cave rockshelters evidence of occupation',
            'Quarry exploitation type',
            'Quarry raw material',
            'Cemetery or grave',
            'Cemetery or graves topography',
            'Cemetery or graves mortuary features',
            'Grave number of graves',
            'Grave type', 'Grave type of human remains',
            'Grave estimated number of individuals',
            'Grave age groups', 'Grave sexes', 'Grave number of female sex',
            'Grave number of male sex', 'Grave number of not specified sex',
            'Grave manipulations of graves', 'Description', 'Reference',
            'Comment'
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
            'Research event',
            'Finds type',
            'Small finds category',
            'Small finds type',
            'Botany species',
            'Animal remains species',
            'Animal remains completeness',
            'Animal remains part',
            'Lithics technology',
            'Lithics industry',
            'Lithics core shape',
            'Lithics retouched tools',
            'Lithics unretouched tools',
            'Lithics raw material',
            'Obsidian',
            'Obsidian amount',
            'Pottery form',
            'Pottery detail',
            'Pottery decoration',
            'Pottery type',
            'Amount',
            'Material',
            'Confidence',
            'Reference',
            'Comment',
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


class ResearchEventDownloadView(GenericListView):
    model = ResearchEvent
    table_class = ResearchEventTable
    template_name = 'browsing/researchevent_list_generic.html'
    filter_class = ResearchEventListFilter
    formhelper_class = GenericFilterFormHelper

    def render_to_response(self, context, **kwargs):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='text/csv')
        filename = "defc_research_events_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(filename)
        writer = csv.writer(response, delimiter=",")
        writer.writerow([
            'Research event ID', 'Research type',
            'Institution', 'Year of activity start year',
            'Year of activity end year', 'Project name', 'Project id',
            'Project leader', 'Special analysis',
            'Reference', 'Comment']
        )
        for obj in self.get_queryset():
            writer.writerow([obj.id,
                            '; '.join([str(obj) for obj in obj.research_type.all()]),
                            '; '.join([str(obj) for obj in obj.institution.all()]),
                            obj.year_of_activity_start_year,
                            obj.year_of_activity_end_year,
                            obj.project_name,
                            obj.project_id,
                            obj.project_leader,
                            '; '.join([str(obj) for obj in obj.special_analysis.all()]),
                            '; '.join([str(obj) for obj in obj.reference.all()]),
                            obj.comment])
        return response


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


class InterpretationDownloadView(GenericListView):
    model = Interpretation
    table_class = InterpretationTable
    template_name = 'browsing/interpretation_list_generic.html'
    filter_class = InterpretationListFilter
    formhelper_class = GenericFilterFormHelper

    def render_to_response(self, context, **kwargs):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='text/csv')
        filename = "defc_interpretations_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(filename)
        writer = csv.writer(response, delimiter=",")
        writer.writerow([
            'Interpretation ID', 'Area',
            'Finds', 'Description',
            'Production type', 'Subsistence type',
            'Reference', 'Comment']
        )
        for obj in self.get_queryset():
            writer.writerow([obj.id,
                            '; '.join([str(obj) for obj in obj.area.all()]),
                            '; '.join([str(obj) for obj in obj.finds.all()]),
                            obj.description,
                            '; '.join([str(obj) for obj in obj.production_type.all()]),
                            '; '.join([str(obj) for obj in obj.subsistence_type.all()]),
                            '; '.join([str(obj) for obj in obj.reference.all()]),
                            obj.comment])
        return response


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
