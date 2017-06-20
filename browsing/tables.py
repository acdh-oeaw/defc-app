import django_tables2 as tables
from django_tables2.utils import A
from defcdb.models import Site, Area, Finds, Interpretation
from django.utils.html import format_html

TEMPLATE = """
<ul>
  {% for p in period_list %}
  <li>{p} something<li></br>
  {% endfor %}
</ul>
 """


class SiteTable(tables.Table):
    site_id = tables.LinkColumn('publicrecords:site_detail', args=[A('pk')], accessor='id')
    name = tables.LinkColumn('publicrecords:site_detail', args=[A('pk')], verbose_name='site name')
    province_name = tables.Column(accessor='province.name', verbose_name='district')

    class Meta:
        model = Site
        fields = ['site_id', 'name', 'province.region', 'province_name']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class AreaTable(tables.Table):
    area_type = tables.LinkColumn('publicrecords:area_detail', args=[A('pk')])
    period = tables.TemplateColumn(template_name='browsing/templateColumn.html')
    area_id = tables.LinkColumn('publicrecords:area_detail', args=[A('pk')], accessor='id')
    site_name = tables.Column(accessor='site.name', verbose_name='site name')

    class Meta:
        model = Area
        fields = ['area_id', 'area_type', 'site_name', 'period']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class FindsTable(tables.Table):
    finds_id = tables.LinkColumn('publicrecords:finds_detail', args=[A('pk')], accessor='id')
    finds_description = tables.LinkColumn(
        'publicrecords:finds_detail', args=[A('pk')],
        verbose_name='finds type')
    site_name = tables.Column(accessor='area.site.name', verbose_name='site name')

    class Meta:
        model = Finds
        fields = ['finds_id', 'finds_description', 'site_name']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class ResearchEventTable(tables.Table):
    researchevent_id = tables.LinkColumn(
        'publicrecords:researchevent_detail', args=[A('pk')], accessor='id')
    research_type = tables.LinkColumn(
        'publicrecords:researchevent_detail', args=[A('pk')], empty_values=())
    # research_type = tables.LinkColumn(empty_values=())

    def render_research_type(self, record):
        if record.research_type.all():
            return ', '.join([rtype.name for rtype in record.research_type.all()])
        return '-'

    class Meta:
        model = Finds
        fields = ['researchevent_id', 'research_type', 'project_name']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class InterpretationTable(tables.Table):
    interpretation_id = tables.LinkColumn(
        'publicrecords:interpretation_detail', args=[A('pk')], accessor='id')
    production_type = tables.Column(empty_values=())
    subsistence_type = tables.Column(empty_values=())
    area__site__name = tables.Column(empty_values=(), verbose_name='Site')

    def render_production_type(self, record):
        if record.production_type.all():
            return ', '.join([ptype.name for ptype in record.production_type.all()])
        return '-'

    def render_subsistence_type(self, record):
        if record.subsistence_type.all():
            return ', '.join([stype.name for stype in record.subsistence_type.all()])
        return '-'

    def render_area__site__name(self, record):
        if record.area.all():
            first_site = record.area.all()[0].site
            return first_site.name
        #     return ', '.join([area.site.name for area in record.area.all()])
        # return '-'

    class Meta:
        model = Interpretation
        fields = ['interpretation_id', 'production_type', 'subsistence_type']
        attrs = {"class": "table table-hover table-striped table-condensed"}
