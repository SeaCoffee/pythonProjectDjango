from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer1, UserSerializer2
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission


class ProfileCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class AuthMeView(generics.RetrieveAPIView):
     permission_classes = (IsAuthenticated,)

     def retrieve(self, request, *args, **kwargs):
         serializer = self.get_serializer(request.user)
         return Response(serializer.data)

class AdminToUserView(generics.UpdateAPIView):
     permission_classes = (IsAdminUser,)

     def put(self, request, *args, **kwargs):
         user = request.user
         user.is_superuser = False
         user.save()
         return Response({'status': 'ok'})


class UserListView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer2

class BlockUserView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)

    def put(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        user = User.objects.get(pk=user_id)
        user.is_active = False
        user.save()
        return Response({'status': 'ok'})

class UnblockUserView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)

    def put(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        user = User.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        return Response({'status': 'ok'})


class IsSuperuser(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class BlockAdminView(generics.UpdateAPIView):
    permission_classes = (IsSuperuser,)

    def put(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        user = User.objects.get(pk=user_id)
        user.is_active = False
        user.save()
        return Response({'status': 'ok'})

class UnblockAdminView(generics.UpdateAPIView):
    permission_classes = (IsSuperuser,)

    def put(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        user = User.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        return Response({'status': 'ok'})
