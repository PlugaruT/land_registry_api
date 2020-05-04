import os
from io import StringIO

from django.test import TestCase
from django.core.management import call_command


class HousePricesTest(TestCase):
    def test_get_with_no_params(self):
        out = StringIO()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        call_command("seed_db", file_path=f"{dir_path}/test-data.csv", stdout=out)

        response = self.client.get("/api/v1/house-prices")

        expected = {
            "data": {
                "2017-08-01": {
                    "average_price": 688333.3333333334,
                    "property_type": "Flats",
                },
                "2017-06-01": {"average_price": 420250.0, "property_type": "Flats"},
                "2017-09-01": {
                    "average_price": 418285.71428571426,
                    "property_type": "Flats",
                },
                "2017-12-01": {"average_price": 500000.0, "property_type": "Flats"},
                "2017-10-01": {"average_price": 1117500.0, "property_type": "Flats"},
                "2017-11-01": {"average_price": 420000.0, "property_type": "Flats"},
            }
        }
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), expected)

    def test_get_with_invalid_from_date(self):
        response = self.client.get("/api/v1/house-prices", {"from_date": "invalid"})

        self.assertEquals(response.status_code, 400)
        self.assertTrue("error" in response.json())

    def test_get_with_invalid_to_date(self):
        response = self.client.get("/api/v1/house-prices", {"to_date": "invalid"})

        self.assertEquals(response.status_code, 400)
        self.assertTrue("error" in response.json())


class TransactionsTest(TestCase):
    def test_get_with_no_params(self):
        response = self.client.get("/api/v1/transactions")

        self.assertEquals(response.status_code, 200)

    def test_get_with_invalid_from_date(self):
        response = self.client.get("/api/v1/transactions", {"from_date": "invalid"})

        self.assertEquals(response.status_code, 400)
        self.assertTrue("error" in response.json())

    def test_get_with_invalid_to_date(self):
        response = self.client.get("/api/v1/transactions", {"to_date": "invalid"})

        self.assertEquals(response.status_code, 400)
        self.assertTrue("error" in response.json())
