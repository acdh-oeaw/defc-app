import django_filters
from defcdb.models import Site

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


class SiteListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    province__region__name = django_filters.CharFilter(lookup_expr='icontains')
    province__name = django_filters.CharFilter(lookup_expr='icontains')
    topography__name = django_filters.CharFilter(lookup_expr='icontains')
    reference__author = django_filters.CharFilter(lookup_expr='icontains')
    reference__title = django_filters.CharFilter(lookup_expr='icontains')
    period = django_filters.MethodFilter(action='my_custom_filter')

    class Meta:
        model = Site
        fields = ['name', 'topography', 'province']

    def my_custom_filter(self, queryset, value):
            return Site.objects.filter(area__period__period_name__icontains=value)
