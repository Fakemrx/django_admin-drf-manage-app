from django.contrib import admin
from django.urls import reverse, reverse_lazy
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from SalesNetwork.models.additional_information import SellersNetwork, Contacts, Country, Address, Products, Workers
from SalesNetwork.models.network_links import Factory, Distributor, Dealership, Retailer, IndividualSeller


@admin.action(description='Снять задолженности у выбранных продавцов')
def debt_reset(modeladmin, request, queryset):
    queryset.update(debt='0')


class IndividualSellerAdmin(admin.ModelAdmin):
    def get_provider_url(self, object):
        return mark_safe(f"<a href='{f'/admin/SalesNetwork/sellersnetwork/{object.get_provider.info.id}'}'>"
                         f"{object.get_provider}</a>" if object.get_provider else 'Нет поставщика')

    list_display = ['info', 'get_provider_url']
    list_filter = ('info__contacts__address__city',)
    get_provider_url.short_description = 'Поставщик'

    class Meta:
        model = IndividualSeller


class RetailerAdmin(admin.ModelAdmin):
    def get_provider_url(self, object):
        return mark_safe(f"<a href='{f'/admin/SalesNetwork/sellersnetwork/{object.get_provider.info.id}'}'>"
                         f"{object.get_provider}</a>" if object.get_provider else 'Нет поставщика')

    list_display = ['info', 'get_provider_url']
    list_filter = ('info__contacts__address__city',)
    get_provider_url.short_description = 'Поставщик'

    class Meta:
        model = Retailer


class DealershipAdmin(admin.ModelAdmin):
    def get_provider_url(self, object):
        return mark_safe(f"<a href='{f'/admin/SalesNetwork/sellersnetwork/{object.get_provider.info.id}'}'>"
                         f"{object.get_provider}</a>" if object.get_provider else 'Нет поставщика')

    list_display = ['info', 'get_provider_url']
    list_filter = ('info__contacts__address__city',)
    get_provider_url.short_description = 'Поставщик'

    class Meta:
        model = Dealership


class DistributorAdmin(admin.ModelAdmin):
    def get_provider_url(self, object):
        return mark_safe(f"<a href='{f'/admin/SalesNetwork/sellersnetwork/{object.get_provider.info.id}'}'>"
                         f"{object.get_provider}</a>" if object.get_provider else 'Нет поставщика')

    list_display = ['info', 'get_provider_url']
    list_filter = ('info__contacts__address__city',)
    get_provider_url.short_description = 'Поставщик'

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
