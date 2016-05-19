import django_filters
from defcdb.models import Site, DC_site_topography, DC_region, DC_province, Area, DC_area_areatype
from defcdb.models import Finds,DC_finds_type,DC_researchevent_researchtype, ResearchEvent, Interpretation, DC_researchevent_institution
from defcdb.models import DC_interpretation_productiontype, DC_interpretation_subsistencetype
from .forms import SiteFilterForm


django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


# def get_names():
#     SITE_CHOICES = []
#     for x in Site.objects.all():
#         pairs = (x.name, x.name)
#         SITE_CHOICES.append(pairs)
#     return set(SITE_CHOICES)


class SiteListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', help_text=False)
    province__region__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_region.objects.all(), label='Region', help_text=False
    )
    province = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_province.objects.all(), label='District', help_text=False
    )
    topography__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_site_topography.objects.all(), label='Topography', help_text=False
    )
    #reference__author = django_filters.CharFilter(lookup_expr='icontains')
    #reference__title = django_filters.CharFilter(lookup_expr='icontains')
    period = django_filters.MethodFilter(action='my_custom_filter', help_text=False)

    class Meta:
        model = Site
        form = SiteFilterForm
        fields = ['province']
        # order_by = (
        #     ('name', 'Site name'),
        #     ('province', 'District')
        #     )

    def my_custom_filter(self, queryset, value):
            return queryset.filter(area__period__period_name__icontains=value).distinct()


class AreaListFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='icontains') no name field in area class
    site__province__region__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_region.objects.all(), label='Region', help_text=False
    )
    site__province = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_province.objects.all(), label='District', help_text=False
    )
    area_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_areatype.objects.all(), help_text=False
    )
    site__name = django_filters.CharFilter(lookup_expr='icontains', help_text=False)
    period = django_filters.MethodFilter(action='my_custom_filter', help_text=False)

    class Meta:
        model = Area
        fields = ['area_type']

    def my_custom_filter(self, queryset, value):
        return queryset.filter(period__period_name__icontains=value).distinct()


class FindsListFilter(django_filters.FilterSet):
    finds_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_finds_type.objects.all(), help_text=False
        )
    area__site__province = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_province.objects.all(), label='District', help_text=False
    )
    area__site__name = django_filters.CharFilter(lookup_expr='icontains',
        label='Site name',help_text=False)
    area__area_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_area_areatype.objects.all(),
        label='Area type', help_text=False
        )
    period = django_filters.MethodFilter(action='my_custom_filter', help_text=False)
    research_event__research_type__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_researchevent_researchtype.objects.all(),
        label='Research type', help_text=False
        )

    class Meta:
        model = Finds
        fields = ['finds_type']

    def my_custom_filter(self, queryset, value):
        return queryset.filter(area__period__period_name__icontains=value).distinct()


class ResearchEventListFilter(django_filters.FilterSet):
    research_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_researchevent_researchtype.objects.all(), help_text=False
        )
    institution = django_filters.MethodFilter(action='my_custom_filter', help_text=False)
    year_of_activity_start_year = django_filters.NumberFilter(
        lookup_expr='exact', help_text=False, label='Start year of research activity'
        )
    year_of_activity_end_year = django_filters.NumberFilter(
        lookup_expr='exact', help_text=False, label='End year of research activity'
        )
    project_name = django_filters.CharFilter(lookup_expr='icontains',help_text=False)
    finds__area__site__name = django_filters.CharFilter(lookup_expr='icontains',
        label='Site name',help_text=False)

    class Meta:
        model = ResearchEvent
        fields = ['research_type']

    def my_custom_filter(self, queryset, value):
        return queryset.filter(institution__name__icontains=value).distinct()


class InterpretationListFilter(django_filters.FilterSet):
    production_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_interpretation_productiontype.objects.all(), help_text=False
        )
    subsistence_type = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_interpretation_subsistencetype.objects.all(), help_text=False
        )
    area__site__name = django_filters.CharFilter(lookup_expr='icontains',
        label='Site name',help_text=False)

    class Meta:
        model = Interpretation
        fields = ['production_type']












