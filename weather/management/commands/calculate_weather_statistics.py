# your_app/management/commands/calculate_weather_statistics.py

import os
from django.core.management.base import BaseCommand
from django.db.models import Avg, Sum
from weather.models import Weather, WeatherStatistics

class Command(BaseCommand):
    help = 'Calculate and store weather statistics for each year and station'

    def handle(self, *args, **kwargs):
        WeatherStatistics.objects.all().delete()  # Clear previous statistics

        weather_data = Weather.objects.values('station', 'date__year').annotate(
            avg_max_temp=Avg('maximum_temperature'),
            avg_min_temp=Avg('minimum_temperature'),
            total_precipitation=Sum('precipitation')
        )

        for data in weather_data:
            station = data['station']
            year = data['date__year']
            avg_max_temp = data['avg_max_temp']
            avg_min_temp = data['avg_min_temp']
            total_precipitation = data['total_precipitation']

            # Convert precipitation from tenths of a millimeter to centimeters
            if total_precipitation is not None:
                total_precipitation = total_precipitation / 100

            WeatherStatistics.objects.create(
                station=station,
                year=year,
                average_maximum_temperature=avg_max_temp,
                average_minimum_temperature=avg_min_temp,
                total_accumulated_precipitation=total_precipitation
            )

        self.stdout.write(self.style.SUCCESS('Successfully calculated and stored weather statistics'))
