from rest_framework import generics

from SalesNetwork.models.additional_information import SellersNetwork
from SalesNetwork.serializers import UDSellersNetworkSerializer, CreateSellersNetworkSerializer


class NetworkAPICreate(generics.CreateAPIView):
    serializer_class = CreateSellersNetworkSerializer
    queryset = SellersNetwork.objects.all()


class NetworkAPIDeleteUpdate(generics.DestroyAPIView, generics.UpdateAPIView):
    serializer_class = UDSellersNetworkSerializer
    queryset = SellersNetwork.objects.all()
