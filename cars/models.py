from django.db import models

class CarModel(models.Model):
    car_brand = models.CharField(max_length=100)
    year_of_manufacture = models.IntegerField()
    number_of_seats = models.IntegerField()
    body_type = models.CharField(max_length=100)
    engine_capacity = models.FloatField()
    price = models.IntegerField()