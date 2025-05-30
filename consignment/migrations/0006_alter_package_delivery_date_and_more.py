# Generated by Django 4.2 on 2025-05-31 16:34

import consignment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0005_alter_package_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='delivery_date',
            field=models.DateField(blank=True, default=consignment.models.default_delivery_date, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='shipping_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
