from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.core import validators

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class usersSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    class Meta:
        model = users
        fields = '__all__'
    def get_username(self, instance):
        return instance.user.username
    def get_first_name(self, instance):
        return instance.user.first_name
    def get_last_name(self, instance):
        return instance.user.last_name


class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMAIL_VERIFICATION
        fields = "__all__"