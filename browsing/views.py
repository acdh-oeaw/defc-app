from django_tables2 import SingleTableView, RequestConfig
from defcdb.models import Site

from .filters import SiteListFilter
from .forms import GenericFilterFormHelper
from .tables import SiteTable


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

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
