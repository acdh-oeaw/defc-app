import django_tables2 as tables
from django_tables2.utils import A
from defcdb.models import Site, Area


class SiteTable(tables.Table):
    name = tables.LinkColumn('publicrecords:site_detail', args=[A('pk')])

    class Meta:
        model = Site
        fields = ['name', 'province']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class AreaTable(tables.Table):
    area_type = tables.LinkColumn('publicrecords:area_detail', args=[A('pk')])

    class Meta:
        model = Area
        fields = ['id', 'area_type', 'site']
        attrs = {"class": "table table-hover table-striped table-condensed"}