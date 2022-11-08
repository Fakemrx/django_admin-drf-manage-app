from django.contrib import admin
from SalesNetwork.models.additional_information import SellersNetwork, Contacts, Country, Address, Products, Workers
from SalesNetwork.models.network_links import Factory, Distributor, Dealership, Retailer, IndividualSeller

admin.site.register(Factory)
admin.site.register(Distributor)
admin.site.register(Dealership)
admin.site.register(Retailer)
admin.site.register(IndividualSeller)
admin.site.register(SellersNetwork)
admin.site.register(Contacts)
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Products)
admin.site.register(Workers)
