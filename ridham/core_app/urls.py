from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'core_app'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile', views.user_profile, name='user_profile'),
]