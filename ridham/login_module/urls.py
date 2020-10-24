from django.urls import path
from . import views

app_name = 'login_module'
urlpatterns = [
    path('', views.loginForm, name='loginForm'),
]