from django.contrib import admin
from .models import Food, FoodCategory, Cuisine
# Register your models here.

admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(Cuisine)
