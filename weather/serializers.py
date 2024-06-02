# your_app/serializers.py

from rest_framework import serializers
from .models import Weather, WeatherStatistics

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class WeatherStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStatistics
        fields = '__all__'
