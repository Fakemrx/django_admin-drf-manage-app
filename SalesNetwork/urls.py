from django.urls import path

from SalesNetwork.views.list_filter import NetworkAPIView, NetworkDebtFilterAPIView
from SalesNetwork.views.network import NetworkAPIDeleteUpdate, NetworkAPICreate
from SalesNetwork.views.product import ProductAPICreate, ProductAPIDeleteUpdate

urlpatterns = [
    path('list/', NetworkAPIView.as_view(), name='list'),
    path('avg_debt_filter/', NetworkDebtFilterAPIView.as_view(), name='avg-debt'),
    path('create/sellers_network/', NetworkAPICreate.as_view(), name='create-sellers-network'),
    path('delete_update/sellers_network/<int:pk>', NetworkAPIDeleteUpdate.as_view(), name='delete-update-sellers-network'),
    path('create/product', ProductAPICreate.as_view(), name='create-product'),
    path('delete_update/product/<int:pk>', ProductAPIDeleteUpdate.as_view(), name='delete-update-product'),
]