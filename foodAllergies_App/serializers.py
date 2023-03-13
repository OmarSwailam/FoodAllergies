from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.core import validators

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'
