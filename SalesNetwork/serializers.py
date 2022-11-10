from rest_framework import serializers

from SalesNetwork.models.additional_information import SellersNetwork, Address, Contacts, Country, Products, Workers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)


class AddressSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Address
        fields = ('country', 'city', 'street', 'house')


class ContactsSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Contacts
        fields = ('email', 'address')


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'prod_model', 'release_date')


class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ('name',)


class NetworkSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(read_only=True)
    products = ProductsSerializer(many=True)
    workers = WorkersSerializer(many=True)

    class Meta:
        model = SellersNetwork
        fields = ('name', 'contacts', 'products', 'workers', 'debt', 'creation_time')


class NetworkAvgFilterSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(read_only=True)

    class Meta:
        model = SellersNetwork
        fields = ('name', 'contacts', 'debt')


class UDSellersNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellersNetwork
        fields = ('name', 'contacts', 'products', 'workers')


class CreateSellersNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellersNetwork
        fields = ('name', 'contacts', 'products', 'workers', 'debt')


class CUDProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'prod_model', 'release_date')
