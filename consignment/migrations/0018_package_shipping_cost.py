# Generated by Django 5.1 on 2024-10-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0017_remove_package_delivery_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='shipping_cost',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
