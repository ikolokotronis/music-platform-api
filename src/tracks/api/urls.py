from django.urls import path
from .views import TrackView, TrackDetailView

app_name = "tracks"

urlpatterns = [
    path("", TrackView.as_view(), name="track_view"),
    path("<int:pk>/", TrackDetailView.as_view(), name="track_detail"),
]
