from django.urls import path
from .views import ProxyConsumerView

urlpatterns = [
    path('', ProxyConsumerView.as_view(), name='consumer_home'),
]
