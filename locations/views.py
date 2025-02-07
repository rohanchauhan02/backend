import logging
from django.db import IntegrityError
from rest_framework.exceptions import NotFound
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer

# Set up logging
logger = logging.getLogger(__name__)


class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            logger.error(f"IntegrityError while creating locations: {str(e)}", exc_info=True)
            return Response(
                {"error": "Duplicate entry detected.", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            logger.error(f"Unexpected error in LocationListCreateView: {str(e)}", exc_info=True)
            return Response(
                {"error": "An unexpected error occurred.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class LocationBulkCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            return Response(
                {"error": "Expected a list of locations."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=request.data, many=True)

        try:
            serializer.is_valid(raise_exception=True)
            locations = [Location(**data) for data in serializer.validated_data]
            Location.objects.bulk_create(locations, ignore_conflicts=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            logger.error(f"IntegrityError in LocationBulkCreateView: {str(e)}", exc_info=True)
            return Response(
                {"error": "Duplicate entry detected.", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            logger.error(f"Unexpected error in LocationBulkCreateView: {str(e)}", exc_info=True)
            return Response(
                {"error": "An unexpected error occurred.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class LocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Location deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class LocationRetrieveUpdateDestroyByCode(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = "unloc_code"

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving location with unloc_code {kwargs.get('unloc_code')}: {str(e)}", exc_info=True)
            return Response(
                {"error": "An unexpected error occurred.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=self.partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)

        except IntegrityError as e:
            logger.error(f"IntegrityError while updating location {kwargs.get('unloc_code')}: {str(e)}", exc_info=True)
            return Response(
                {"error": "Duplicate entry detected.", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            logger.error(f"Unexpected error while updating location {kwargs.get('unloc_code')}: {str(e)}", exc_info=True)
            return Response(
                {"error": "An unexpected error occurred.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(
                {"message": "Location deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            logger.error(f"Error deleting location with unloc_code {kwargs.get('unloc_code')}: {str(e)}", exc_info=True)
            return Response(
                {"error": "An unexpected error occurred.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
