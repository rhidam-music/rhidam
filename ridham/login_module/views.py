from django.http import request
from django.shortcuts import render

# Create your views here.
def loginForm(request):
    return render(request, 'login_module/loginFile.html')

def loginAction(request):
    
    pass

def forgotPassAction(request):
    pass

def createUserAction(request):
    pass

def createUserView(request):
    pass

def forgotPassView(request):
    pass