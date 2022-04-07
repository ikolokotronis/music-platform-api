from django.urls import path
from .views import (
    TrackView, TrackDetailView
)

app_name = 'tracks'

urlpatterns = [
    path('', TrackView.as_view(), name='track-list'),
    path('<int:pk>/', TrackDetailView.as_view(), name='track-detail'),
]
