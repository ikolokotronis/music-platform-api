from django.urls import path
from users.api.views import (
    RegistrationView,
)

app_name = 'users'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
]
