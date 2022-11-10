from django.urls import path
from SalesNetwork.views import NetworkAPIView, ProductAPICreate, FactoryAPICreate, DealershipAPICreate,\
    DistributorAPICreate, RetailerAPICreate, IndividualSellerAPICreate, NetworkDebtFilterAPIView

urlpatterns = [
    path('list/', NetworkAPIView.as_view(), name='list'),
    path('avg_debt_filter/', NetworkDebtFilterAPIView.as_view(), name='avg-debt'),
    path('create/product', ProductAPICreate.as_view(), name='create-product'),
    path('create/factory', FactoryAPICreate.as_view(), name='create-factory'),
    path('create/distributor', DistributorAPICreate.as_view(), name='create-distributor'),
    path('create/dealership', DealershipAPICreate.as_view(), name='create-dealership'),
    path('create/retailer', RetailerAPICreate.as_view(), name='create-retailer'),
    path('create/individual_seller', IndividualSellerAPICreate.as_view(), name='create-individual_seller'),
]