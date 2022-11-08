from django.shortcuts import render
from rest_framework import generics

from SalesNetwork.models.additional_information import SellersNetwork
from SalesNetwork.serializers import NetworkSerializer


class NetworkAPIView(generics.ListAPIView):
    queryset = SellersNetwork.objects.all()
    serializer_class = NetworkSerializer
