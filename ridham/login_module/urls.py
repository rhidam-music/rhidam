from django.urls import path
from . import views

app_name = 'login_module'
urlpatterns = [
    path('login', views.login, name='login'),
    path('forgot_password', views.forgotPassword, name='forgotPassword'),
    path('create_a_new_account', views.createUserAccount, name='createUserAccount')
]