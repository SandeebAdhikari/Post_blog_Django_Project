from . import views
from django.urls import path

urlpatterns = [
    path('', views.schedulerList, name='schedulerList'),
    path('create/', views.scheduleCreate, name='scheduleCreate'),
    path('<int:scheduler_id>/edit/', views.scheduleEdit, name='scheduleEdit'),
    path('<int:scheduler_id>/delete/', views.scheduleDelete, name='scheduleDelete'),
     path('register/', views.register, name='register'),
] 