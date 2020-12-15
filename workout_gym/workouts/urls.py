from django.urls import path
from . import views

urlpatterns = [
   path('', views.workouts_home, name='workouts_home'),
   path('w_o_create', views.w_o_create, name='w_o_create'),
   path('<int:pk>', views.WorkoutsDetailView.as_view(), name='workouts-detail'),
   path('<int:pk>/update', views.NewsUpdateView.as_view(), name='workouts-update'),
   path('<int:pk>/delete', views.WorkoutsDeleteView.as_view(), name='workouts-delete'),

]