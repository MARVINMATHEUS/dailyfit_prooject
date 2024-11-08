
from django.db import models
from core.models import ModelBase
from django.contrib.auth.models import User

class Category(ModelBase):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Exercise(ModelBase):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="exercise")
    description = models.TextField()
    difficulty_level = models.CharField(max_length=20, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])

    def __str__(self):
        return f"{self.name} - {self.category.name}"

class Workout(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    name = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class WorkoutItem(ModelBase):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="items")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets  = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    weight  = models.FloatField(blank=True, null=True)
    rest  = models.DurationField(blank=True, null=True)

    def __str__(self):
        return f"{self.exercise.name} - {self.workout.name}"
