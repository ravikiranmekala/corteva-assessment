# your_app/views.py

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Weather, WeatherStatistics
from .serializers import WeatherSerializer, WeatherStatisticsSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all().order_by('date', 'station')
    serializer_class = WeatherSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['station', 'date']
    ordering_fields = ['date', 'station']

class WeatherStatisticsViewSet(viewsets.ModelViewSet):
    queryset = WeatherStatistics.objects.all().order_by('year', 'station')
    serializer_class = WeatherStatisticsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['station', 'year']
    ordering_fields = ['year', 'station']
