from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users
from serializers import *
from rest_framework import viewsets
from .models import *
from rest_framework.permissions import IsAuthenticated

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['car'] = self.request.user.car
        serializer.save()


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer

