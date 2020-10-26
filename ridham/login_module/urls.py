from django.urls import path
from . import views

app_name = 'login_module'
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('forgot_password/', views.forgotPassword, name='forgot_password'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]