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
    fields = modelclass._meta.get_fields()
    serialized = []
    for f in fields:
        if f.get_internal_type() == "ManyToManyField":
            attrs = getattr(modelclass, f.name)
            values = "|".join([y[1] for y in attrs.values_list()])
            key_value = values
        else:
            key_value = getattr(modelclass, f.name)
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
        filename = "editions_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(filename)
        writer = csv.writer(response, delimiter=",")
        # writer.writerow([x.name for x in Site._meta.get_fields()])
        # for x in self.get_queryset():
        #     row = serialize(x)
        #     writer.writerow(row)
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
