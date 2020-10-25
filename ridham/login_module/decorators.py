from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login_module:dashboard')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_roles).exists():
                #This user has (at least) one group that meets authorisation requirement
                return view_func(request, *args, **kwargs)

            else:
                #no group found for this user..
                return HttpResponse('You are not authorised to view this page')
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

def admins_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.exists():
            group = request.user.groups.all()[0]
            if group == 'admins':
                return view_func(request, *args, **kwargs) 
            else:
                return HttpResponse('You are not authorised to view this page')
    return wrapper_func