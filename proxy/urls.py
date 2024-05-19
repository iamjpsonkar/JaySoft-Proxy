from django.urls import path
from .views import (
    ProxyView, SignupView, SigninView
)

urlpatterns = [
    path('', ProxyView.as_view(), name='proxy_home'),
    path('signup/', SignupView.as_view(), name='proxy_signup'),
    path('signin/', SigninView.as_view(), name='proxy_signin'),
]
