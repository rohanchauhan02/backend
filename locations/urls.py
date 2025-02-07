from django.urls import path
from .views import (
    LocationListCreateView,
    LocationBulkCreateView,
    LocationRetrieveUpdateDestroyView,
    LocationRetrieveUpdateDestroyByCode,
)

urlpatterns = [
    # Using Generic Views
    path("", LocationListCreateView.as_view(), name="location-list-create"),
    path("bulk-import/", LocationBulkCreateView.as_view(), name="location-bulk-import"),
    path(
        "<int:pk>/", LocationRetrieveUpdateDestroyView.as_view(), name="location-detail"
    ),
    path(
        "codes/<str:unloc_code>/",
        LocationRetrieveUpdateDestroyByCode.as_view(),
        name="location-detail-bycode",
    ),
]
