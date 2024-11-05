from django.contrib import admin
from django.urls import path
from home1 import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('Signup', views.Signup, name='Signup'),
    path('Login', views.Login, name='Login'),
    path('home', views.home2, name='home2'),
    path('Logout', views.Logout, name='Logout'),
    path('index', views.index, name='index')
    
]