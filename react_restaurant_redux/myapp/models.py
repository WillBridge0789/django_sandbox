from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.ForeignKey("FoodPrice", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("FoodCategory", on_delete=models.SET_NULL, null=True)
    cuisine = models.ForeignKey("Cuisine", on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class FoodPrice(models.Model):
    cost = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(500)],)

    def __str__(self):
        return self.cost

class FoodCategory(models.Model):
    national_origin = models.CharField(max_length=200) 

    def __str__(self):
        return self.national_origin

class Cuisine(models.Model):
    # make this field name more appropriate. Cuisine is the model. Weird to have the field_name also be cuisine. 
    # it's a label or a name or a title
    # cuisine type?
    cuisine_type = models.CharField(max_length=200)

    def __str__(self):
        return self.cuisine_type