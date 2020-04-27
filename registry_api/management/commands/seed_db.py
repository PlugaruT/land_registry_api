from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Seed DB with data from CSV file'

    def handle(self, *args, **options):
        print("hello")