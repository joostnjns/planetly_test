from django.db import models

# Create your models here.
class TemperaturesByCity(models.Model):
    dt = models.CharField(max_length=10)
    averagetemperature = models.DecimalField(max_digits = 12, decimal_places=10)
    averagetemperatureuncertainty = models.DecimalField(max_digits=12, decimal_places=10)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()