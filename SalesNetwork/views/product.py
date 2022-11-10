from rest_framework import generics

from SalesNetwork.models.additional_information import Products
from SalesNetwork.serializers import CUDProductSerializer


class ProductAPICreate(generics.CreateAPIView):
    serializer_class = CUDProductSerializer


class ProductAPIDeleteUpdate(generics.DestroyAPIView, generics.UpdateAPIView):
    serializer_class = CUDProductSerializer
    queryset = Products.objects.all()
