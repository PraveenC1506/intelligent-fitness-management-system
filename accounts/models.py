
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
    meal = models.CharField(max_length=50)
    food_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
    protein = models.FloatField(default=0)

    def __str__(self):
        return f"{self.food_name} ({self.meal})"


class Profile(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    age = models.PositiveIntegerField(null=True, blank=True)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    emergency_contact = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"