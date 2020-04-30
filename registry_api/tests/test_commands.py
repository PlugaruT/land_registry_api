import os
from io import StringIO

from django.test import TestCase
from django.core.management import call_command

from registry_api.models import LandTransaction


class SeedDBTest(TestCase):
    def test_seed_db_valid_path(self):
        out = StringIO()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        call_command("seed_db", file_path=f"{dir_path}/test-data.csv", stdout=out)

        self.assertEquals(LandTransaction.objects.all().count(), 16)

    def test_seed_db_invalid_path(self):
        out = StringIO()
        call_command("seed_db", file_path="random_parh", stdout=out)

        self.assertIn("File path is invalid!", out.getvalue())
