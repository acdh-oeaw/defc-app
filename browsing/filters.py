import django_filters
from defcdb.models import Site, DC_site_topography, DC_region, DC_province, Area, DC_area_areatype
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

