import django_filters
from .models import *


class FileFilter(django_filters.FilterSet):
    country__name = django_filters.CharFilter(lookup_expr='icontains')
    crmProduct__name = django_filters.CharFilter(lookup_expr='icontains')
    mysheetId = django_filters.NumberFilter()

    class Meta:
        model = File
        fields = ['country__name', 'crmProduct__name', 'mysheetId']
