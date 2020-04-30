import os

from django.core.management.base import BaseCommand, CommandError
from django.db import connection


class Command(BaseCommand):
    help = "Seed DB with data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument("--file_path", type=str, required=True)

    def handle(self, *args, **options):
        file_path = options.get("file_path")

        if not os.path.isfile(file_path):
            self.stdout.write(self.style.ERROR("File path is invalid!"))
            return

        sql = """
            COPY registry_api_landtransaction(transaction_id,price,date_of_transfer,postcode,property_type, property_age,duration,paon,saon,street,locality,town,district,county,category_type,record_status)
            FROM %s WITH (DELIMITER ',', QUOTE '"', FORMAT 'csv');
        """

        self.stdout.write(
            self.style.SUCCESS(
                f"Importing '{file_path}' into DB. Please wait, it will take some time."
            )
        )
        with connection.cursor() as cursor:
            cursor.execute(sql, [file_path])

        self.stdout.write(self.style.SUCCESS("All done!"))
