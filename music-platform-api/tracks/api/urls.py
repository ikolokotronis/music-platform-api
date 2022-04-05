from django.urls import path
from posts.api import views
from .views import (
    TrackList, TrackDetail
)

app_name = 'tracks'

urlpatterns = [
    path('', TrackList.as_view(), name='track-list'),
    path('<int:pk>/', TrackDetail.as_view(), name='track-detail'),
]
