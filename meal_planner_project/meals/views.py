from django.shortcuts import render
from .models import Meal

def meal_list(request):
    meals = Meal.objects.all()
    return render(request, 'meals/meal_list.html', {'meals': meals})

def create_meals(request):
    meal1 = Meal.objects.create(name='Spaghetti', description='Delicious pasta dish')
    meal2 = Meal.objects.create(name='Salad', description='Healthy green salad')
    return render(request, 'create_meals.html')


