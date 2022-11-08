from rest_framework import serializers

from SalesNetwork.models.additional_information import SellersNetwork, Address, Contacts, Country, Products, Workers
from SalesNetwork.models.network_links import Factory, IndividualSeller


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


# class FactorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Factory
#         fields = ('info',)

class IndividualSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualSeller
        fields = ('info', 'factory_provider', 'distributor_provider', 'dealership_provider', 'retailer_provider')


class NetworkSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(read_only=True)
    # ProductsSerializer(read_only=True)
    # WorkersSerializer(read_only=True)
    provider = IndividualSellerSerializer(read_only=True)

    class Meta:
        model = SellersNetwork
        fields = ('name', 'contacts', 'products', 'workers', 'provider', 'debt', 'creation_time')
