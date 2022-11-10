from rest_framework import serializers

from SalesNetwork.models.additional_information import SellersNetwork, Address, Contacts, Country, Products, Workers
from SalesNetwork.models.network_links import Factory, Distributor, Dealership, Retailer, IndividualSeller


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


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'prod_model', 'release_date')

    def create(self, validated_data):
        product = Products.objects.create(
            name=validated_data.get('name', None),
            prod_model=validated_data.get('prod_model', None),
            release_date=validated_data.get('release_date', None)
        )
        return product


class CreateFactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ('info',)

    def create(self, validated_data):
        factory = Factory.objects.create(
            info=validated_data.get('info', None),
        )
        return factory


class CreateDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ('info', 'factory_provider')

    def create(self, validated_data):
        distributor = Distributor.objects.create(
            info=validated_data.get('info', None),
            factory_provider=validated_data.get('factory_provider', None),
        )
        return distributor


class CreateDealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealership
        fields = ('info', 'factory_provider', 'distributor_provider')

    def create(self, validated_data):
        dealership = Dealership.objects.create(
            info=validated_data.get('info', None),
            factory_provider=validated_data.get('factory_provider', None),
            distributor_provider=validated_data.get('distributor_provider', None),
        )
        return dealership


class CreateRetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ('info', 'factory_provider', 'distributor_provider', 'dealership_provider')

    def create(self, validated_data):
        retailer = Retailer.objects.create(
            info=validated_data.get('info', None),
            factory_provider=validated_data.get('factory_provider', None),
            distributor_provider=validated_data.get('distributor_provider', None),
            dealership_provider=validated_data.get('dealership_provider', None),
        )
        return retailer


class CreateIndividualSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualSeller
        fields = ('info', 'factory_provider', 'distributor_provider', 'dealership_provider', 'retailer_provider')

    def create(self, validated_data):
        individual_seller = IndividualSeller.objects.create(
            info=validated_data.get('info', None),
            factory_provider=validated_data.get('factory_provider', None),
            distributor_provider=validated_data.get('distributor_provider', None),
            dealership_provider=validated_data.get('dealership_provider', None),
            retailer_provider=validated_data.get('retailer_provider', None),
        )
        return individual_seller
