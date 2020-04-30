from django.test import TestCase


class HousePricesTest(TestCase):
    def test_get_with_no_params(self):
        response = self.client.get("/api/v1/house-prices")

        self.assertEquals(response.status_code, 200)

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
