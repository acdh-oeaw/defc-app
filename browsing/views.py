from django_tables2 import SingleTableView, RequestConfig
from defcdb.models import Site, DC_chronological_system

from .filters import SiteListFilter
from .forms import GenericFilterFormHelper
from .tables import SiteTable


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
