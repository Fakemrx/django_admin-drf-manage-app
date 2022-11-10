from django.urls import path
from SalesNetwork.views import NetworkAPIView, ProductAPICreate, FactoryAPICreate, DealershipAPICreate, \
    DistributorAPICreate, RetailerAPICreate, IndividualSellerAPICreate, NetworkDebtFilterAPIView, ProductAPIDelete, \
    FactoryAPIDelete, IndividualSellerAPIDelete, RetailerAPIDelete, DealershipAPIDelete, DistributorAPIDelete

urlpatterns = [
    path('list/', NetworkAPIView.as_view(), name='list'),
    path('avg_debt_filter/', NetworkDebtFilterAPIView.as_view(), name='avg-debt'),
    path('create/product', ProductAPICreate.as_view(), name='create-product'),
    path('delete/product/<int:pk>', ProductAPIDelete.as_view(), name='delete-product'),
    path('create/factory', FactoryAPICreate.as_view(), name='create-factory'),
    path('delete/factory/<int:pk>', FactoryAPIDelete.as_view(), name='delete-factory'),
    path('create/distributor', DistributorAPICreate.as_view(), name='create-distributor'),
    path('delete/distributor/<int:pk>', DistributorAPIDelete.as_view(), name='delete-distributor'),
    path('create/dealership', DealershipAPICreate.as_view(), name='create-dealership'),
    path('delete/dealership/<int:pk>',  DealershipAPIDelete.as_view(), name='delete-dealership'),
    path('create/retailer', RetailerAPICreate.as_view(), name='create-retailer'),
    path('delete/retailer/<int:pk>', RetailerAPIDelete.as_view(), name='delete-retailer'),
    path('create/individual_seller', IndividualSellerAPICreate.as_view(), name='create-individual_seller'),
    path('delete/individual_seller/<int:pk>', IndividualSellerAPIDelete.as_view(), name='delete-individual_seller'),
]