from django.contrib import admin
from django.urls import path
from passgen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('password/', views.passgen, name='passgen'),  # URL for the password generator
]
