import django_filters
from defcdb.models import Site, DC_site_topography, DC_region, DC_province
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


def get_names():
    SITE_CHOICES = []
    for x in Site.objects.all():
        pairs = (x.name, x.name)
        SITE_CHOICES.append(pairs)
    return set(SITE_CHOICES)


class SiteListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    province__region__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_region.objects.all()
    )
    province = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_province.objects.all()
    )
    topography__name = django_filters.ModelMultipleChoiceFilter(
        queryset=DC_site_topography.objects.all()
    )
    #reference__author = django_filters.CharFilter(lookup_expr='icontains')
    #reference__title = django_filters.CharFilter(lookup_expr='icontains')
    period = django_filters.MethodFilter(action='my_custom_filter')

    class Meta:
        model = Site
        form = SiteFilterForm
        fields = ['province']

    def my_custom_filter(self, queryset, value):
            return queryset.filter(area__period__period_name__icontains=value).distinct()
