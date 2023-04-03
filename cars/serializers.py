from rest_framework import serializers
from .models import CarModel

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'car_brand', 'year_of_manufacture')

    def delete(self, instance):
        instance.delete()

    def create(self, validated_data):
        return CarModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.car_brand = validated_data.get('car_brand', instance.car_brand)
        instance.year_of_manufacture = validated_data.get('year_of_manufacture', instance.year_of_manufacture)
        instance.save()
        return instance

