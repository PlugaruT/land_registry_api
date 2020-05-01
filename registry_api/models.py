from django.db import models


class LandTransaction(models.Model):
    transaction_id = models.CharField(max_length=200)
    price = models.BigIntegerField()
    date_of_transfer = models.DateTimeField()
    postcode = models.CharField(max_length=100)
    property_type = models.CharField(max_length=10)
    property_age = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    paon = models.CharField(max_length=100)
    saon = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    category_type = models.CharField(max_length=10)
    record_status = models.CharField(max_length=10)
