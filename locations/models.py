from django.db import models

class Locations(models.Model):
    unloc_code = models.CharField(max_length=10, unique=True, null=True, blank=True)  # Allow null for now
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    port_code = models.CharField(max_length=10, null=True, blank=True)
    alias = models.JSONField(default=list, blank=True)
    regions = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = "locations"

    def __str__(self):
        return f"{self.name}, {self.city}, {self.country}"
