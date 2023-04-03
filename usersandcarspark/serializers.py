from .models import *

from rest_framework import serializers

class UsersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        brand = Cars
        fields = "__all__"