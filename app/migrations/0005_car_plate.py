# Generated by Django 5.1.6 on 2025-02-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_car_brand_alter_car_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
