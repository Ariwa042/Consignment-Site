# Generated by Django 4.2 on 2024-10-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0010_remove_ship_latitude_remove_ship_longitude_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ship',
            options={'verbose_name': 'Ship', 'verbose_name_plural': 'Ships'},
        ),
        migrations.RemoveField(
            model_name='ship',
            name='map_url',
        ),
        migrations.AddField(
            model_name='ship',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='tracking_code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='receiving_location',
            field=models.URLField(blank=True, help_text='URL for destination map iframe', null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='sending_location',
            field=models.URLField(blank=True, help_text='URL for sending location map iframe', null=True),
        ),
        migrations.DeleteModel(
            name='TrackingCode',
        ),
    ]