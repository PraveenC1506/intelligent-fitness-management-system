

from datetime import date, timedelta




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    return render(request, 'accounts/home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def features(request):
    return render(request, 'accounts/features.html')

def membership(request):
    return render(request, 'accounts/membership.html')

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def login(request):
    return render(request,'accounts/login.html')


def create_account(request):
    return render(request,'accounts/register.html')





from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'accounts/login.html')


@login_required
def progress_tracker(request):
    return render(request, 'accounts/progress_tracker.html')

def food_tracker(request):
    return render(request, 'accounts/food_tracker.html')

def home_workouts(request):
    return render(request, 'accounts/home_workouts.html')

def gym_workouts(request):
    return render(request, 'accounts/gym_workouts.html')

def profile(request):
    return render(request, 'accounts/profile.html')



from django.shortcuts import render

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def progress_tracker(request):
    return render(request, 'accounts/progress_tracker.html')

# def food_tracker(request):
#     return render(request, 'accounts/food_tracker.html')

def home_workouts(request):
    return render(request, 'accounts/home_workouts.html')

def gym_workouts(request):
    return render(request, 'accounts/gym_workouts.html')

def logout(request):
    return render(request,'accounts/logout.html')




from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def workout_tracker(request):
     return render(request,'accounts/workout_tracker.html')

def food(request):
    return render(request, 'accounts/food_tracker.html')

def gym_workouts(request):
    return render(request,'accounts/gym_workout.html')

def home_workout(request):
    return render(request,'accounts/home_workout.html')

# def logout_view(request):
#     return redirect(request,'accounts/.logout.html')










from django.shortcuts import render

# def food_tracker(request):
#     return render(request,'accounts/food_tracker.html')


def home_workouts(request):
    return render(request, 'accounts/home_workouts.html')


def gym_workouts(request):
    return render(request,'accounts/gym_workouts.html')

def logout(request):
    return render(request,'accounts/logout.html')







from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Workout

@login_required
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









from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout

@login_required
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

    return render(request, "accounts/edit_workout.html", {
        "workout": workout
    })









@login_required
def delete_workout(request, id):
    workout = get_object_or_404(
        Workout,
        id=id,
        user=request.user
    )
    workout.delete()
    return redirect("workout_tracker")




@login_required
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











from datetime import date, timedelta
from .models import FoodLog









@login_required
def food_tracker(request):
    selected_date=request.GET.get("date")
    foods = FoodLog.objects.filter(user=request.user)

    if selected_date:
        foods = foods.filter(food_date=selected_date)

    return render(
        request,
        "accounts/food_tracker.html",
        {
            "foods": foods,
            "selected_date": selected_date,
        }
    )


@login_required
def add_food(request):
    if request.method == "POST":
        FoodLog.objects.create(
            user=request.user,
            food_date=request.POST["date"],
            meal=request.POST["meal"],
            food_name=request.POST["food_name"],
            quantity=request.POST["quantity"],
            calories=request.POST["calories"],
            protein=request.POST.get("protein", 0),
        )

    return redirect("food_tracker")


@login_required
def edit_food(request, id):
    food = get_object_or_404(FoodLog, id=id, user=request.user)

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
        {"food": food}
    )




@login_required
def delete_food(request, id):
    food = get_object_or_404(FoodLog, id=id, user=request.user)
    food.delete()
    return redirect("food_tracker")





from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})

    return render(request, 'accounts/login.html')






@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')



from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )
                return redirect('login')  # MUST BE HERE

    return render(request, 'accounts/register.html')




from django.shortcuts import render, redirect

def join_view(request):
    return render(request, 'accounts/join.html')




def logout(request):
    return render(request,'accounts/logout.html')




from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validation
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
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()

            messages.success(request, "Registration successful. Please login.")
            return redirect('login')

        except IntegrityError:
            messages.error(request, "Username already exists")
            return redirect('register')

    return render(request, 'accounts/register.html')




