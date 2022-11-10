from django_filters import rest_framework as filters
from SalesNetwork.models.additional_information import SellersNetwork


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class NetworkFilter(filters.FilterSet):
    contacts = CharFilterInFilter(field_name='contacts__address__city', lookup_expr='in')
    products = filters.BaseInFilter(field_name='products__id', lookup_expr='in')

    class Meta:
        model = SellersNetwork
        fields = ['contacts', 'products']
