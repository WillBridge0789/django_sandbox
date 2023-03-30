from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.ForeignKey("Food", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    name = models.ForeignKey("Food", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name