from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_date = models.DateField(default=now)
    exercise_name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField(default=0)

    def __str__(self):
        return f"{self.exercise_name} ({self.workout_date})"
    









class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_date = models.DateField(default=now)
    meal = models.CharField(max_length=50)          # Breakfast/Lunch/Dinner
    food_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()        # grams
    calories = models.PositiveIntegerField()
    protein = models.FloatField(default=0)

    def __str__(self):
        return f"{self.food_name} ({self.meal})"