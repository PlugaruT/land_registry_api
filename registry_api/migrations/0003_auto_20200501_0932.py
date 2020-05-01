# Generated by Django 3.0.5 on 2020-05-01 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry_api', '0002_auto_20200427_1810'),
    ]

    operations = [
        migrations.RunSQL(
        """
        CREATE INDEX postcode_idx ON registry_api_landtransaction (postcode);
        """
        )
    ]
