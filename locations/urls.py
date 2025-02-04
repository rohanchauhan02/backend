from django.urls import path
from .views import (
    LocationListCreateView,
    LocationRetrieveUpdateDestroyView,
    LocationRetrieveUpdateDestroyByCode,
)

urlpatterns = [
    # Using Generic Views
    path("", LocationListCreateView.as_view(), name="location-list-create"),
    path(
        "<int:pk>/", LocationRetrieveUpdateDestroyView.as_view(), name="location-detail"
    ),
    path(
        "codes/<str:unloc_code>/",
        LocationRetrieveUpdateDestroyByCode.as_view(),
        name="location-detail-bycode",
    ),
]
