from django.urls import path
from .views import ProxyServerView

urlpatterns = [
    path('', ProxyServerView.as_view(), name='proxy_server'),
]
