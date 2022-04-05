from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.api.views import (
    RegistrationView,
    AccountView
)

app_name = 'users'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('properties/<int:pk>/', AccountView.as_view(), name='properties'),
    path('register/', RegistrationView.as_view(), name='register'),
]
