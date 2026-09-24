
from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Main pages
    path('dashboard/', views.dashboard, name='dashboard'),
    path('features/', views.features, name='features'),
    path('membership/', views.membership, name='membership'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),

    # Workout pages
    path('gym_workouts/', views.gym_workouts, name='gym_workouts'),
    path('home_workouts/', views.home_workouts, name='home_workouts'),
    path('home_workout/', views.home_workout, name='home_workout'),
    path('workout_tracker/', views.workout_tracker, name='workout_tracker'),

    # Workout CRUD
    path('workout/add/', views.add_workout, name='add_workout'),
    path('workout/edit/<int:id>/', views.edit_workout, name='edit_workout'),
    path('workout/delete/<int:id>/', views.delete_workout, name='delete_workout'),

    # Food
    path('food/', views.food_tracker, name='food_tracker'),
    path('food/add/', views.add_food, name='add_food'),
    path('food/edit/<int:id>/', views.edit_food, name='edit_food'),
    path('food/delete/<int:id>/', views.delete_food, name='delete_food'),

    # Other
    path('progress_tracker/', views.progress_tracker, name='progress_tracker'),
    path('join/', views.join_view, name='join'),
]