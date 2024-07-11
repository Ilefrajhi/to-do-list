from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = "login"),
    path('register/', views.register, name = "register"),
    path('reset_password/', views.reset_password, name = "reset_password"),
    path('logout/', views.logout, name = "logout"),
    path('main/', views.main, name = "main"),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('add_user/', views.add_user, name='add_user'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('incomplete_tasks/', views.incomplete_tasks, name='incomplete_tasks'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('search/', views.search_tasks, name='search_tasks'),
    path('login_user/', views.login_user, name='login_user'), 
]