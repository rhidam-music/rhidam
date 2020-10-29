from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import CreateUserForm, ForgotForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admins_only

'''
my 3 wrappers -> @unauthenticated_user, @allowed_users, @admins_only
'''

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if(request.method == "POST"):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                # gp = Group.objects.get(name='customer')
                # user.groups.add(gp)
                uname = user.username
                messages.success(request, "Account successfully created for " +uname+   " !")
                return redirect('login_module:login')
            except:
                messages.info("There is already an account with this email id! ")
                return redirect('login_module:register')
    

    context = {'form' : form}
    return render(request, 'login_module/createAcc.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('core_app:dashboard')
        else:
            messages.info(request, "Invalid username or Password")

    context = {}
    return render(request, 'login_module/loginFile.html', context)

@login_required(login_url='login_module:login')
def dashboard(request):
    context = {}
    return render(request, 'core_app/dashboard.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login_module:login')
