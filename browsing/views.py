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
