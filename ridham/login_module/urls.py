from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login_module'
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]