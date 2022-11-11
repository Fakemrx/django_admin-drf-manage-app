from rest_framework import generics

from SalesNetwork.models.additional_information import Products
from SalesNetwork.permissions import IsAuthenticatedAndWorking
from SalesNetwork.serializers import CUDProductSerializer


class ProductAPICreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedAndWorking]
    serializer_class = CUDProductSerializer


class ProductAPIDeleteUpdate(generics.DestroyAPIView, generics.UpdateAPIView):
    permission_classes = [IsAuthenticatedAndWorking]
    serializer_class = CUDProductSerializer
    queryset = Products.objects.all()
