from django.http import request
from django.shortcuts import render
from .models import User, LoginHistory
def login(request):
    if request.method == 'GET':
        return render(request, 'login_module/loginFile.html')
    else:
        try:
            lgtry = request.POST['lgtry']
        except:
            return render(request, 'login_module/loginFile.html')
        if lgtry[0] == '1':
            userInputUserName = request.POST['username']
            userInputPassword = request.POST['password']
            print(userInputPassword, userInputUserName)
            #TODO : Proper Exception Handling for invalid cases
            try:
                user = User.objects.get(userName=userInputUserName, passWord=userInputPassword)
            except User.DoesNotExist:
                return render(request, 'login_module/loginFile.html')
            return render(request, 'login_module/loginSuccess.html')

        else:
            return render(request, 'login_module/loginFile.html')

def forgotPassword(request):
    return render(request, 'login_module/forgotPassword.html')

def createUserAccount(request):
    return render(request, 'login_module/createAcc.html')
