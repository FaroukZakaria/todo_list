from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontend, name='frontend'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
]