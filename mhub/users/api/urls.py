from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.api.views import (
    RegistrationView,
)

app_name = 'users'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]
