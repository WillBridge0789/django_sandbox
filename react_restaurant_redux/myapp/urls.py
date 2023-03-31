from django.urls import path

from . import views

urlpatterns = [
    path('myapp/', views.Food, name='index'),
]