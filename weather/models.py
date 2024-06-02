from django.db import models


class Weather(models.Model):
    station = models.CharField(max_length=50)
    date = models.DateField()
    maximum_temperature = models.FloatField(null=True)
    minimum_temperature = models.FloatField(null=True)
    precipitation = models.FloatField(null=True)

    class Meta:
        unique_together = (('station', 'date'),)

class WeatherStatistics(models.Model):
    station = models.CharField(max_length=50)
    year = models.IntegerField()
    average_maximum_temperature = models.FloatField(null=True)
    average_minimum_temperature = models.FloatField(null=True)
    total_accumulated_precipitation = models.FloatField(null=True)

    class Meta:
        unique_together = (('station', 'year'),)