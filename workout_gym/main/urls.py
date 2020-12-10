from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.login, name='login'),
   path('', views.index, name='home'),
   path('workouts/', views.workouts, name='workouts')
]