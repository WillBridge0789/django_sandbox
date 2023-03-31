from django.shortcuts import render

# Create your views here.
from .models import Food, FoodCategory, Cuisine
from django.http import HttpResponse


def foodItem(request, food_id):
    return HttpResponse("%s" % food_id)

def foodPrice(request, price_id):
    return HttpResponse('%d' % price_id)

def foodCategory(request, category_id):
    return HttpResponse("%s" % category_id)

def foodCuisine(request, cuisine_id):
    return HttpResponse("%s" % cuisine_id)