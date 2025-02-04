import os
import json
import requests
from django.core.management.base import BaseCommand
from locations.models import Locations


class Command(BaseCommand):
    help = "Import locations from JSON into the database"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="Path to the JSON file or URL")

    def handle(self, *args, **kwargs):
        json_file = kwargs["json_file"]

        # Check if json_file is a URL or local path
        if json_file.startswith("http://") or json_file.startswith("https://"):
            self.stdout.write(self.style.NOTICE(f"Downloading JSON data from {json_file}"))
            response = requests.get(json_file)

            if response.status_code != 200:
                self.stderr.write(self.style.ERROR(f"Failed to fetch URL: {json_file}"))
                return

            try:
                data = response.json()
            except json.JSONDecodeError:
                self.stderr.write(self.style.ERROR("Invalid JSON received"))
                return
        else:
            if not os.path.exists(json_file):
                self.stderr.write(self.style.ERROR(f"File not found: {json_file}"))
                return

            with open(json_file, "r", encoding="utf-8") as file:
                data = json.load(file)

        # Process JSON data
        for unloc_code, value in data.items():
            Location.objects.update_or_create(
                unloc_code=unloc_code,  # Unique identifier for each location
                defaults={
                    "name": value.get("name"),
                    "city": value.get("city"),
                    "province": value.get("province"),
                    "country": value.get("country"),
                    "timezone": value.get("timezone"),
                    "latitude": value["coordinates"][1] if "coordinates" in value else None,
                    "longitude": value["coordinates"][0] if "coordinates" in value else None,
                    "port_code": value.get("code"),
                    "alias": value.get("alias", []),
                    "regions": value.get("regions", []),
                },
            )

        self.stdout.write(self.style.SUCCESS("Successfully imported locations from JSON"))
