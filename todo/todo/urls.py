from django.contrib import admin
from django.urls import path, include

# Make sure you import your webapp's urls correctly
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')), 
    path('register', include('webapp.urls')),
    path('login', include('webapp.urls')),
    path('logout', include('webapp.urls')),
    path('reset_password', include('webapp.urls')),
]