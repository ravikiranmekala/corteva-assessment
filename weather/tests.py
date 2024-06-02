# your_app/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Weather, WeatherStatistics
import datetime


class WeatherAPITestCase(APITestCase):

    def setUp(self):
        # print('in setup')
        self.sample_weather_data = [
            {'station': 'WS001', 'date': '2022-06-01', 'maximum_temperature': 25.0, 'minimum_temperature': 15.0,
             'precipitation': 5.0},
            {'station': 'WS001', 'date': '2022-06-02', 'maximum_temperature': 27.0, 'minimum_temperature': 16.0,
             'precipitation': 4.5},
            {'station': 'WS002', 'date': '2022-06-01', 'maximum_temperature': 22.0, 'minimum_temperature': 14.0,
             'precipitation': 6.0},
        ]

        # print('before weather create')
        for data in self.sample_weather_data:
            # print('before weather create 1')
            Weather.objects.create(**data)

        self.sample_statistics_data = [
            {'station': 'WS001', 'year': 2022, 'average_maximum_temperature': 26.0, 'average_minimum_temperature': 15.5,
             'total_accumulated_precipitation': 9.5},
            {'station': 'WS002', 'year': 2022, 'average_maximum_temperature': 22.0, 'average_minimum_temperature': 14.0,
             'total_accumulated_precipitation': 6.0},
        ]

        for data in self.sample_statistics_data:
            WeatherStatistics.objects.create(**data)

    def test_create_weather_record(self):
        print('running test_create_weather_record')
        url = reverse('weather-list')
        new_weather_data = {'station': 'WS003', 'date': '2022-06-03', 'maximum_temperature': 30.0,
                            'minimum_temperature': 20.0, 'precipitation': 2.0}
        response = self.client.post(url, new_weather_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Weather.objects.count(), 4)
        self.assertEqual(Weather.objects.get(station='WS003').maximum_temperature, 30.0)

    def test_get_weather_records_no_filters(self):
        url = reverse('weather-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)

    def test_get_weather_records_with_station_filter(self):
        url = reverse('weather-list') + '?station=WS001'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['station'], 'WS001')

    def test_get_weather_records_pagination(self):
        url = reverse('weather-list') + '?page_size=2'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertIn('next', response.data)

    def test_create_weather_statistics_record(self):
        url = reverse('weatherstats-list')
        new_statistics_data = {'station': 'WS003', 'year': 2022, 'average_maximum_temperature': 28.0,
                               'average_minimum_temperature': 18.0, 'total_accumulated_precipitation': 5.0}
        response = self.client.post(url, new_statistics_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WeatherStatistics.objects.count(), 3)
        self.assertEqual(WeatherStatistics.objects.get(station='WS003').average_maximum_temperature, 28.0)

    def test_get_weather_statistics_no_filters(self):
        url = reverse('weatherstats-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_weather_statistics_with_station_filter(self):
        url = reverse('weatherstats-list') + '?station=WS001'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['station'], 'WS001')

    def test_get_weather_statistics_pagination(self):
        url = reverse('weatherstats-list') + '?page_size=1'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertIn('next', response.data)
