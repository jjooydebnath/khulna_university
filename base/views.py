from django.shortcuts import render

def homeView(request):
    return render(request, 'base/home.html')

def notActiveUser(request):
    return render(request, 'base/not-active.html')
