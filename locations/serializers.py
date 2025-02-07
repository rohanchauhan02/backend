from rest_framework import serializers
from .models import Location
import logging

logger = logging.getLogger(__name__)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

    def create(self, validated_data):
        logger.debug(f"Validated data: {validated_data}")
        if isinstance(validated_data, list):
            return Location.objects.bulk_create([Location(**item) for item in validated_data])
        return super().create(validated_data)
