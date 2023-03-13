from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.

class users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=None)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    is_doctor = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class Allergy(models.Model):
    id = models.AutoField(primary_key=True)
    allergy_pic = models.ImageField(upload_to='Allergy_pics', blank=True, null=True)
    arabicDescription = models.TextField(max_length=500)
    englishDescription = models.TextField(max_length=500)
    arabicName = models.CharField(max_length=50)
    englishName = models.CharField(max_length=50)
    arabicSymptoms = models.TextField(max_length=255)
    englishSymptoms = models.TextField(max_length=255)
    arabicPrevention = models.TextField(max_length=255)
    englishPrevention = models.TextField(max_length=255)
    def __str__(self):
        return f"{self.arabicName} - {self.englishName}"

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    arabicName = models.CharField(max_length=50)
    englishName = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.arabicName} - {self.englishName}"

class Food(models.Model):
    id = models.AutoField(primary_key=True)
    arabicName = models.TextField(max_length=500)
    englishName = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.arabicName} - {self.englishName}"

class FoodAllergy(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.food} - {self.allergy}"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)