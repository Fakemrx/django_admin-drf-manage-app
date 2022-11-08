from django.urls import path
from SalesNetwork.views import NetworkAPIView

urlpatterns = [
    path('list/', NetworkAPIView.as_view(), name='list')
]