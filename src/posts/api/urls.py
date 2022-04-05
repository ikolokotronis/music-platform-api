from django.urls import path
from posts.api import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostView.as_view(), name='post_view'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]
