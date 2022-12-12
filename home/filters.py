import django_filters
from .models import *


class FileFilter(django_filters.FilterSet):
    country__name = django_filters.CharFilter(lookup_expr='icontains')
    product__name = django_filters.CharFilter(lookup_expr='icontains')
    productId = django_filters.NumberFilter()

    class Meta:
        model = File
        fields = ['country__name', 'product__name', 'productId']
