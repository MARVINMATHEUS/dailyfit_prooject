from django.db import models
from django.contrib.auth.models import User
from core.models import ModelBase

class Food(ModelBase):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    fats = models.FloatField()

    def __str__(self):
        return self.name

class Meal(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meals")
    name = models.CharField(max_length=50)
    foods = models.ManyToManyField(Food, through='MealItem')

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class MealItem(ModelBase):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.food.name} - {self.meal.name}"
