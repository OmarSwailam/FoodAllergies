from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.core import validators
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

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
    
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    
class FoodAllergySerializer(serializers.ModelSerializer):
    food = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    allegry = serializers.SerializerMethodField()

    class Meta:
        model = FoodAllergy
        fields = '__all__'

    def get_food(self, obj):
        food = obj.food
        dataofFood = {
             'arabicName' : food.arabicName,
             'englishName' : food.englishName
         }
        return dataofFood
    
    def get_category(self, obj):
        category = obj.category
        dataofcategory = {
             'arabicName' : category.arabicName,
             'englishName' : category.englishName
         }
        return dataofcategory
    
    def get_allergy(self, obj):
        allegry = obj.allegry
        dataofallegry = {
             'allergy_pic' : allegry.allergy_pic,
             'arabicDescription' : allegry.arabicDescription,
             'englishDescription' : allegry.englishDescription,
             'arabicName' : allegry.arabicName,
             'englishName' : allegry.englishName,
             'arabicSymptoms' : allegry.arabicSymptoms,
             'englishSymptoms' : allegry.englishSymptoms,
             'arabicPrevention' : allegry.arabicPrevention,
             'englishPrevention' : allegry.englishPrevention,
         }
        return dataofallegry
    







        
class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMAIL_VERIFICATION
        fields = "__all__"



# class CustomField(FoodAllergy):
#     def to_native(self, obj):
#         return obj.self.all()