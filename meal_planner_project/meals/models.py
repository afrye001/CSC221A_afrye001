from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    meal = models.OneToOneField(Meal, on_delete=models.CASCADE)
