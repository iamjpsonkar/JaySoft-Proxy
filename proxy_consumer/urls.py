from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='proxy_consumer_home'),
]
