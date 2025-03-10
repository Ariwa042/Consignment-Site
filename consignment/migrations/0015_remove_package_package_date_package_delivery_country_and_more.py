# Generated by Django 5.1 on 2024-10-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0014_remove_package_pdf_package_package_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='package_date',
        ),
        migrations.AddField(
            model_name='package',
            name='delivery_country',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='from_country',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='shipping_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
