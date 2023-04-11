"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from cars.views import CarModelViewSet
from usersandcarspark.views import *
from profilephoto.views import ProfileCreateView, AuthMeView, AdminToUserView, UserListView, BlockUserView, UnblockUserView, BlockAdminView, UnblockAdminView
from profilephoto.serializers import UserSerializer1, UserSerializer2


router = routers.DefaultRouter()
router.register(r'carmodels', CarModelViewSet, basename='carmodels')

router = routers.SimpleRouter()
router.register(r'usersandcars', UsersViewSet)
router.register(r'profiles', ProfileCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'cars'), namespace='cars')),
    #path('api/usersandcars/', UsersViewSet.as_view({'get': 'list'})),
    #path('api/usersandcars/<int:pk>/', UsersViewSet.as_view({'put': 'update'})),

    path('api/', include(router.urls, 'usersandcars')),
    path('api/', include(router.urls, 'cars')),

    path('', include(router.urls)),

    path('profiles/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('auth/me/', AuthMeView.as_view(serializer_class=UserSerializer1), name='auth_me'),

    path('auth/admin-to-user/', AdminToUserView.as_view(), name='admin_to_user'),
    path('users/', UserListView.as_view(), name='user_list'),

    path('users/<int:pk>/block/', BlockUserView.as_view(), name='block_user'),
    path('users/<int:pk>/unblock/', UnblockUserView.as_view(), name='unblock_user'),

path('admins/<int:pk>/block/', BlockAdminView.as_view(), name='block_admin'),
    path('admins/<int:pk>/unblock/', UnblockAdminView.as_view(), name='unblock_admin'),
]



