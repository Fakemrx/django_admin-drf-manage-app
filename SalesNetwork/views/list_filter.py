from decimal import Decimal

from rest_framework import generics
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend

from SalesNetwork.permissions import IsAuthenticatedAndWorking
from SalesNetwork.service import NetworkFilter

from SalesNetwork.models.additional_information import SellersNetwork
from SalesNetwork.serializers import NetworkSerializer, NetworkAvgFilterSerializer


class NetworkAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedAndWorking]
    queryset = SellersNetwork.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NetworkFilter


class NetworkDebtFilterAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedAndWorking]
    avg_debt = SellersNetwork.objects.aggregate(Avg('debt'))['debt__avg']
    if avg_debt:
        avg_debt = avg_debt.quantize(Decimal("1.00"))
    else:
        avg_debt = 0
    queryset = SellersNetwork.objects.filter(debt__gt=avg_debt).values()
    serializer_class = NetworkAvgFilterSerializer