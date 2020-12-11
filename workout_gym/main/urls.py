from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.user_login, name='login'),
   path('logout/', views.user_logout, name='logout'),
   path('', views.index, name='home'),
   path('workouts/', views.workouts, name='workouts')
]