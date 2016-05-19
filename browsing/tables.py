import django_tables2 as tables
from django_tables2.utils import A
from defcdb.models import Site, Area, Finds, ResearchEvent


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


class FindsTable(tables.Table):
    finds_type = tables.LinkColumn('publicrecords:finds_detail', args=[A('pk')])
    finds_id = tables.LinkColumn('publicrecords:finds_detail', args=[A('pk')], accessor='id')

    class Meta:
        model = Finds
        fields = ['finds_id', 'finds_type', 'area.site']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class ResearchEventTable(tables.Table):
    researchevent_id = tables.LinkColumn('publicrecords:researchevent_detail', args=[A('pk')], accessor='id')
    research_type = tables.LinkColumn('publicrecords:researchevent_detail', args=[A('pk')], empty_values=())
    # research_type = tables.LinkColumn(empty_values=())

    def render_research_type(self, record):
        if record.research_type.all():
            return ', '.join([rtype.name for rtype in record.research_type.all()])
        return '-'

    class Meta:
        model = Finds
        fields = ['researchevent_id','research_type', 'project_name']
        attrs = {"class": "table table-hover table-striped table-condensed"}

    

   