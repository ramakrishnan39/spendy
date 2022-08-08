from django.contrib import admin
from django.urls import path,include
from . import views_users

urlpatterns = [
    path('login/', views_users.v_login,name='Login'),
    path('register/',views_users.v_register,name='Register'),
    path('profile/', views_users.v_profile, name="Profile"),
    path('logout/',views_users.v_logout, name="Logout"),
]