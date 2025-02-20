from django.db import models

# Create your models here.

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, default="Unknown Model")
    brand = models.CharField(max_length=200, default="Unknown")
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)