from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.authtoken import views


router = DefaultRouter()

router.register('users', UserViewSet, basename='Users')

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    ]
urlpatterns = urlpatterns + router.urls