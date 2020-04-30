import os
from io import StringIO
import datetime
from pytz import UTC
from decimal import Decimal
from django.test import TestCase
from django.core.management import call_command

from registry_api.models import LandTransaction
from registry_api.queries import get_average_price, get_number_of_transactions


class AveragePriceQueryTest(TestCase):
    def test_average_price_query(self):
        out = StringIO()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        call_command("seed_db", file_path=f"{dir_path}/test-data.csv", stdout=out)

        response = get_average_price()

        expected = [
            {
                "period": datetime.datetime(2017, 8, 1, 0, 0, tzinfo=UTC),
                "average_price": Decimal("688333.333333333333"),
                "property_type": "F",
            },
            {
                "period": datetime.datetime(2017, 6, 1, 0, 0, tzinfo=UTC),
                "average_price": Decimal("420250.000000000000"),
                "property_type": "F",
            },
            {
                "period": datetime.datetime(2017, 9, 1, 0, 0, tzinfo=UTC),
                "average_price": Decimal("418285.714285714286"),
                "property_type": "F",
            },
            {
                "period": datetime.datetime(2017, 12, 1, 0, 0, tzinfo=UTC),
                "average_price": Decimal("500000.000000000000"),
                "property_type": "F",
            },
            {
                "period": datetime.datetime(2017, 10, 1, 0, 0, tzinfo=UTC),
                "average_price": Decimal("1117500.000000000000"),
                "property_type": "F",
            },
            {
                "period": datetime.datetime(2017, 11, 1, 0, 0, tzinfo=UTC),
                "average_price": Decimal("420000.000000000000"),
                "property_type": "F",
            },
        ]

        self.assertEquals(len(response), 6)
        self.assertListEqual(response, expected)


# class NumberOfTransactions(TestCase):
#     def test_number_of_transactions_query(self):
#         out = StringIO()
#         dir_path = os.path.dirname(os.path.realpath(__file__))
#         call_command("seed_db", file_path=f"{dir_path}/test-data.csv", stdout=out)

#         response = get_number_of_transactions()

#         self.assertEquals(len(response), 6)
