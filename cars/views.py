from rest_framework.views import APIView

from rest_framework import viewsets
from .models import CarModel
from .serializers import CarModelSerializer
from rest_framework.response import Response
from rest_framework import status


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    list_serializer_class = CarModelSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer_class
        return super().get_serializer_class()

    def post(self, request):
        serializer = CarModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        car_model = CarModel.objects.get(pk=pk)
        serializer = CarModelSerializer(car_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        car_model = CarModel.objects.get(pk=pk)
        car_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)