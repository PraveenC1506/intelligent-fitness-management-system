
from datetime import date, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError

from .models import Workout, FoodLog


# =========================
# GENERAL PAGES
# =========================

def home(request):
    return render(request, 'accounts/home.html')


def features(request):
    return render(request, 'accounts/features.html')


def membership(request):
    return render(request, 'accounts/membership.html')


def about(request):
    return render(request, 'accounts/about.html')


def contact(request):
    return render(request, 'accounts/contact.html')


def join_view(request):
    return render(request, 'accounts/join.html')


# =========================
# AUTHENTICATION
# =========================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(
            request,
            'accounts/login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required")
            return redirect('register')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters")
            return redirect('register')

        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            messages.success(
                request,
                "Registration successful. Please login."
            )

            return redirect('login')

        except IntegrityError:
            messages.error(request, "Username already exists")
            return redirect('register')

    return render(request, 'accounts/register.html')


def logout_view(request):
    logout(request)
    return redirect('home')


# =========================
# DASHBOARD
# =========================

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


# =========================
# PROFILE
# =========================

@login_required(login_url='login')
def profile(request):
    return render(request, 'accounts/profile.html')


# =========================
# WORKOUT
# =========================

@login_required(login_url='login')
def workout_tracker(request):
    selected_date = request.GET.get("date")

    if selected_date:
        workouts = Workout.objects.filter(
            user=request.user,
            workout_date=selected_date
        )
    else:
        workouts = Workout.objects.filter(
            user=request.user,
            workout_date__gte=date.today() - timedelta(days=30)
        )

    return render(
        request,
        "accounts/workout_tracker.html",
        {
            "workouts": workouts,
            "selected_date": selected_date
        }
    )


@login_required(login_url='login')
def add_workout(request):
    if request.method == "POST":
        Workout.objects.create(
            user=request.user,
            workout_date=request.POST["date"],
            exercise_name=request.POST["exercise_name"],
            sets=request.POST["sets"],
            reps=request.POST["reps"],
            weight=request.POST.get("weight", 0)
        )

    return redirect("workout_tracker")


@login_required(login_url='login')
def edit_workout(request, id):
    workout = get_object_or_404(
        Workout,
        id=id,
        user=request.user
    )

    if request.method == "POST":
        workout.exercise_name = request.POST["exercise_name"]
        workout.sets = request.POST["sets"]
        workout.reps = request.POST["reps"]
        workout.weight = request.POST.get("weight", 0)
        workout.save()

        return redirect("workout_tracker")

    return render(
        request,
        "accounts/edit_workout.html",
        {
            "workout": workout
        }
    )


@login_required(login_url='login')
def delete_workout(request, id):
    workout = get_object_or_404(
        Workout,
        id=id,
        user=request.user
    )

    workout.delete()

    return redirect("workout_tracker")


# =========================
# WORKOUT PAGES
# =========================

@login_required(login_url='login')
def home_workouts(request):
    return render(request, 'accounts/home_workouts.html')


@login_required(login_url='login')
def home_workout(request):
    return render(request, 'accounts/home_workout.html')


@login_required(login_url='login')
def gym_workouts(request):
    return render(request, 'accounts/gym_workouts.html')


# =========================
# FOOD TRACKER
# =========================

@login_required(login_url='login')
def food_tracker(request):
    selected_date = request.GET.get("date")

    foods = FoodLog.objects.filter(
        user=request.user
    )

    if selected_date:
        foods = foods.filter(
            food_date=selected_date
        )

    return render(
        request,
        "accounts/food_tracker.html",
        {
            "foods": foods,
            "selected_date": selected_date
        }
    )


@login_required(login_url='login')
def add_food(request):
    if request.method == "POST":
        FoodLog.objects.create(
            user=request.user,
            food_date=request.POST["date"],
            meal=request.POST["meal"],
            food_name=request.POST["food_name"],
            quantity=request.POST["quantity"],
            calories=request.POST["calories"],
            protein=request.POST.get("protein", 0)
        )

    return redirect("food_tracker")


@login_required(login_url='login')
def edit_food(request, id):
    food = get_object_or_404(
        FoodLog,
        id=id,
        user=request.user
    )

    if request.method == "POST":
        food.meal = request.POST["meal"]
        food.food_name = request.POST["food_name"]
        food.quantity = request.POST["quantity"]
        food.calories = request.POST["calories"]
        food.protein = request.POST.get("protein", 0)

        food.save()

        return redirect("food_tracker")

    return render(
        request,
        "accounts/edit_food.html",
        {
            "food": food
        }
    )


@login_required(login_url='login')
def delete_food(request, id):
    food = get_object_or_404(
        FoodLog,
        id=id,
        user=request.user
    )

    food.delete()

    return redirect("food_tracker")


# =========================
# PROGRESS
# =========================

@login_required(login_url='login')
def progress_tracker(request):
    return render(
        request,
        'accounts/progress_tracker.html'
    )