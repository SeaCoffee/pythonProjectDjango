import django_filters.rest_framework
from django_filters import rest_framework as filters
from .models import CarModel

class CarModelFilter(filters.FilterSet):
    car_brand__startswith = filters.CharFilter(field_name='car_brand', lookup_expr='startswith')
    car_brand__endswith = filters.CharFilter(field_name='car_brand', lookup_expr='endswith')
    car_brand__contains = filters.CharFilter(field_name='car_brand', lookup_expr='icontains')

    class Meta:
        model = CarModel
        fields = ['car_brand']