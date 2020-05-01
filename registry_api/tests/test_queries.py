import os
import datetime
from io import StringIO
from pytz import UTC
from decimal import Decimal

from django.test import TestCase
from django.core.management import call_command

from registry_api.models import LandTransaction
from registry_api.queries import get_average_price, group_transaction_prices


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


class NumberOfTransactions(TestCase):
    def test_number_of_transactions_query(self):
        out = StringIO()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        call_command("seed_db", file_path=f"{dir_path}/test-data.csv", stdout=out)

        response = group_transaction_prices()

        expected = [
            {"bucket": 1, "range": "233500-373687", "cnt": 5},
            {"bucket": 2, "range": "373687-513874", "cnt": 4},
            {"bucket": 3, "range": "513874-654061", "cnt": 2},
            {"bucket": 4, "range": "654061-794248", "cnt": 3},
            {"bucket": 5, "range": "794248-934435", "cnt": 1},
            {"bucket": 9, "range": "1354996-1495183", "cnt": 1},
        ]

        self.assertEquals(len(response), 6)
        self.assertEquals(response, expected)
