from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(users)
admin.site.register(EMAIL_VERIFICATION)
admin.site.register(Allergy)
admin.site.register(Category)
admin.site.register(Food)
# admin.site.register(FoodAllergy)
