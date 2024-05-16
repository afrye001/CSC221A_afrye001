# meals/urls.py

from django.urls import path
from .views import meal_list

urlpatterns = [
    path('', meal_list, name='meal_list'),
]
