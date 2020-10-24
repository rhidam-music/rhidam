from django.http import request
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login_module/loginFile.html')

def forgotPassword(request):
    return render(request, 'login_module/forgotPassword.html')

def createUserAccount(request):
    return render(request, 'login_module/createAcc.html')
