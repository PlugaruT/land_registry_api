# Generated by Django 3.0.5 on 2020-05-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registry_api", "0003_auto_20200501_0932"),
    ]

    operations = [
        migrations.AlterField(
            model_name="landtransaction", name="price", field=models.BigIntegerField(),
        ),
    ]
