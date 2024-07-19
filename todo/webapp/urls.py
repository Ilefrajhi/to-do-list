from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_login_page, name='login'),
    path('register/', views.register, name='register'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('logout/', views.logout, name='logout'),
    path('main/', views.main, name='main'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('add_user/', views.add_user, name='add_user'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('incomplete_tasks/', views.incomplete_tasks, name='incomplete_tasks'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),  # Include <int:task_id> here
    path('search/', views.search_tasks, name='search_tasks'),
    path('login_user/', views.login_user, name='login_user'),
    path('upload/', views.upload_image, name='upload_image'),
    path('success/', views.success, name='success'),
    path('images/', views.display_images, name='display_images'),
    path('test_login_user/', views.test_login_user, name='test_login_user'),

]
