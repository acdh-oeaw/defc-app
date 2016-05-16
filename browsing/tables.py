import django_tables2 as tables
from django_tables2.utils import A
from defcdb.models import Site


class SiteTable(tables.Table):
    name = tables.LinkColumn('publicrecords:site_detail', args=[A('pk')])

    class Meta:
        model = Site
        fields = ['name', 'province']
        attrs = {"class": "table table-hover table-striped table-condensed"}
