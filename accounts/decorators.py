from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_fanc):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_fanc(request, *args, **kwargs)
    return wrapper_func