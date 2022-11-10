from decimal import Decimal

from rest_framework import generics, request
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from SalesNetwork.models.network_links import Factory, Distributor, Dealership, Retailer, IndividualSeller
from SalesNetwork.service import NetworkFilter

from SalesNetwork.models.additional_information import SellersNetwork, Products
from SalesNetwork.serializers import NetworkSerializer, CreateDeleteProductSerializer, CreateDeleteIndividualSellerSerializer, \
    CreateDeleteFactorySerializer, CreateDeleteDealershipSerializer, CreateDeleteDistributorSerializer,\
    CreateDeleteRetailerSerializer, NetworkAvgFilterSerializer


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
    serializer_class = CreateDeleteProductSerializer


class ProductAPIDelete(generics.DestroyAPIView):
    serializer_class = CreateDeleteProductSerializer
    queryset = Products.objects.all()


class FactoryAPICreate(generics.CreateAPIView):
    serializer_class = CreateDeleteFactorySerializer


class FactoryAPIDelete(generics.DestroyAPIView):
    serializer_class = CreateDeleteFactorySerializer
    queryset = Factory.objects.all()


class DistributorAPICreate(generics.CreateAPIView):
    serializer_class = CreateDeleteDistributorSerializer


class DistributorAPIDelete(generics.DestroyAPIView):
    serializer_class = CreateDeleteDistributorSerializer
    queryset = Distributor.objects.all()


class DealershipAPICreate(generics.CreateAPIView):
    serializer_class = CreateDeleteDealershipSerializer


class DealershipAPIDelete(generics.DestroyAPIView):
    serializer_class = CreateDeleteDealershipSerializer
    queryset = Dealership.objects.all()


class RetailerAPICreate(generics.CreateAPIView):
    serializer_class = CreateDeleteRetailerSerializer


class RetailerAPIDelete(generics.DestroyAPIView):
    serializer_class = CreateDeleteRetailerSerializer
    queryset = Retailer.objects.all()


class IndividualSellerAPICreate(generics.CreateAPIView):
    serializer_class = CreateDeleteIndividualSellerSerializer


class IndividualSellerAPIDelete(generics.DestroyAPIView):
    serializer_class = CreateDeleteIndividualSellerSerializer
    queryset = IndividualSeller.objects.all()
