from django.contrib import admin
from SalesNetwork.models.additional_information import SellersNetwork, Contacts, Country, Address, Products, Workers
from SalesNetwork.models.network_links import Factory, Distributor, Dealership, Retailer, IndividualSeller


@admin.action(description='Снять задолженности у выбранных продавцов')
def debt_reset(modeladmin, request, queryset):
    queryset.update(debt='0')


class IndividualSellerAdmin(admin.ModelAdmin):
    list_display = ['info', 'factory_provider', 'distributor_provider', 'dealership_provider', 'retailer_provider']
    list_filter = ('info__contacts__address__city',)

    class Meta:
        model = IndividualSeller


class RetailerAdmin(admin.ModelAdmin):
    list_display = ['info', 'factory_provider', 'distributor_provider', 'dealership_provider']
    list_filter = ('info__contacts__address__city',)

    class Meta:
        model = Retailer


class DealershipAdmin(admin.ModelAdmin):
    list_display = ['info', 'factory_provider', 'distributor_provider']
    list_filter = ('info__contacts__address__city',)

    class Meta:
        model = Dealership


class DistributorAdmin(admin.ModelAdmin):
    list_display = ['info', 'factory_provider']
    list_filter = ('info__contacts__address__city',)

    class Meta:
        model = Distributor


class FactoryAdmin(admin.ModelAdmin):
    list_display = ['info']
    list_filter = ('info__contacts__address__city',)

    class Meta:
        model = Factory


class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'contacts', 'debt', 'creation_time']
    list_filter = ('contacts__address__city',)
    actions = [debt_reset]

    class Meta:
        model = SellersNetwork


admin.site.register(Factory, FactoryAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Dealership, DealershipAdmin)
admin.site.register(Retailer, RetailerAdmin)
admin.site.register(IndividualSeller, IndividualSellerAdmin)
admin.site.register(SellersNetwork, NetworkAdmin)
admin.site.register(Contacts)
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Products)
admin.site.register(Workers)
