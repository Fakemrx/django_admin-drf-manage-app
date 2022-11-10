from decimal import Decimal

from rest_framework import generics, request
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from SalesNetwork.models.network_links import Factory
from SalesNetwork.service import NetworkFilter

from SalesNetwork.models.additional_information import SellersNetwork, Products
from SalesNetwork.serializers import NetworkSerializer, CreateProductSerializer, CreateIndividualSellerSerializer, \
    CreateFactorySerializer, CreateDealershipSerializer, CreateDistributorSerializer,\
    CreateRetailerSerializer, NetworkAvgFilterSerializer


class NetworkAPIView(generics.ListAPIView):
    queryset = SellersNetwork.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NetworkFilter


class NetworkDebtFilterAPIView(generics.ListAPIView):
    avg_debt = SellersNetwork.objects.aggregate(Avg('debt'))['debt__avg']
    avg_debt = avg_debt.quantize(Decimal("1.00"))
    queryset = SellersNetwork.objects.filter(debt__gt=avg_debt).values()
    serializer_class = NetworkAvgFilterSerializer


class ProductAPICreate(generics.CreateAPIView):
    serializer_class = CreateProductSerializer


class ProductAPIDelete(generics.DestroyAPIView):
    serializer_class = CreateProductSerializer
    queryset = Products.objects.all()


class FactoryAPICreate(generics.CreateAPIView):
    serializer_class = CreateFactorySerializer


class DistributorAPICreate(generics.CreateAPIView):
    serializer_class = CreateDistributorSerializer


class DealershipAPICreate(generics.CreateAPIView):
    serializer_class = CreateDealershipSerializer


class RetailerAPICreate(generics.CreateAPIView):
    serializer_class = CreateRetailerSerializer


class IndividualSellerAPICreate(generics.CreateAPIView):
    serializer_class = CreateIndividualSellerSerializer
