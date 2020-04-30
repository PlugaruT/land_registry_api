import os
from io import StringIO

from django.test import TestCase
from django.core.management import call_command

from registry_api.models import LandTransaction
from registry_api.queries import get_average_price, get_number_of_transactions

class AveragePriceQueryTest(TestCase):
        
    def test_average_price_query(self):
        out = StringIO()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        call_command('seed_db', file_path=f'{dir_path}/test-data.csv', stdout=out)
        
        response = get_average_price()

        self.assertEquals(len(response), 6)

        
class NumberOfTransactions(TestCase):

    def test_number_of_transactions_query(self):
        out = StringIO()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        call_command('seed_db', file_path=f'{dir_path}/test-data.csv', stdout=out)
        
        response = get_number_of_transactions()

        self.assertEquals(len(response), 6)