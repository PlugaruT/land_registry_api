import os

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
class Command(BaseCommand):
    help = 'Seed DB with data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        file_path = options.get('file_path')
        
        if not os.path.isfile(file_path):
            print("File path is invalid!")
            return
        
        sql = """
            COPY registry_api_landtransaction(transaction_id,price,date_of_transfer,postcode,property_type, property_age,duration,paon,saon,street,locality,town,district,county,category_type,record_status)
            FROM %s WITH (DELIMITER ',', QUOTE '"', FORMAT 'csv');
        """
        ## '/home/plugaru/Projects/land_registry_api/registry_api/management/commands/data.csv'
        with connection.cursor() as cursor:
            cursor.execute(sql, [file_path])