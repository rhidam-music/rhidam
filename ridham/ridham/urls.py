"""ridham URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core_app.views import HomepageView

urlpatterns = [
    path('', HomepageView),
    path('admin/', admin.site.urls),
    path('dashboard/', include('core_app.urls')),
    path('accounts/', include('login_module.urls')),

    ##forgot password build 
    # 1. submit email form --> PasswordResetView.as_view()
    # 2. email sent success message --> PasswordResetDoneView.as_view()
    # 3. link to password reset form --> PasswordResetConfirmView.as_view()
    # 4. password successfully changed --> PasswordResetCompleteView.as_view()

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name = "login_module/resetPassword.html"), 
    name='reset_password'),

    path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
