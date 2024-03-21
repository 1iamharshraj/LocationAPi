from django.urls import path
from .views import CoordinatesAPIView

urlpatterns = [
    path('coordinates/', CoordinatesAPIView.as_view(), name='coordinates-api'),
]