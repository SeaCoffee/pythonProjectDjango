from django.db import models
from django.core.exceptions import ValidationError

class Cars(models.Model):
    car = models.CharField(max_length=100)
    year = models.IntegerField()

    def clean(self):
        if not self.car:
            raise ValidationError("Field can't be empty")


class Users(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    owner =  models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='cars')

    def clean(self):
        if not self.firstname:
            raise ValidationError("Field can't be empty")





