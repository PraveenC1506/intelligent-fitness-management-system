

from accounts import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('features/', views.features, name='features'),
    path('membership/',views.membership,name='membership'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('gym_workouts/',views.gym_workouts,name='gym_workouts'),
    path('home_workouts/',views.home_workouts,name='home_workouts'),
    path('progress_tracker/',views.progress_tracker,name='progress_tracker'),
    path('food_tracker/',views.food_tracker,name='food_tracker'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.login,name='login'),
]


from django.urls import path
from .views import login_view, dashboard,home,features
from.import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('features/',views.features,name='features'),
    path('membership/',views.membership,name='membership'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('food/',views.food_tracker,name='food_tracker'),
    path('gym_workouts/',views.gym_workouts,name='gym'),
    path('home_workout/',views.home_workout,name='home_workout'),
    path('workout_tracker/', views.workout_tracker, name='workout_tracker'),
    # path('food/',views.food_tracker,name='food_tracker'),
    path('home-workouts/', views.home_workouts, name='home_workouts'),
    path('gym-workkouts/',views.gym_workouts,name='gym_workouts'),
    path("workout/add/", views.add_workout, name="add_workout"),
    path("workout/edit/<int:id>/", views.edit_workout, name="edit_workout"),
    path("workout/delete/<int:id>/", views.delete_workout, name="delete_workout"),
    path("food/add/", views.add_food, name="add_food"),
    path("food/edit/<int:id>/", views.edit_food, name="edit_food"),
    path("food/delete/<int:id>/", views.delete_food, name="delete_food"),
    path('register/',views.register_view,name='register'),
    path('join/',views.join_view,name='join'),
    path('logout/',views.logout,name="logout"),
    path('register/', views.register_view, name='register'),

]








