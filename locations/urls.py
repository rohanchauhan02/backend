
from django.urls import path
from .views import LocationListCreateView, LocationRetrieveUpdateDestroyView

urlpatterns = [
    # Using Generic Views
    path('', LocationListCreateView.as_view(), name='generic-item-list-create'),
    path('/<int:pk>', LocationRetrieveUpdateDestroyView.as_view(), name='generic-item-detail'),
]
