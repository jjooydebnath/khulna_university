from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import User, UserRegistrationForm

def homeView(request):
    return render(request, 'base/home.html')

def notActiveUser(request):
    users = UserRegistrationForm.objects.all()
    return render(request, 'base/not-active.html')

