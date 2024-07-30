from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import CreateUserForm, UserMemberShipForm, StafRegistration
from .models import User, UserRegistrationForm


def loginView(request):
    users = UserRegistrationForm()
    if request.method == "POST":
        user = authenticate(
            mobile_number = request.POST['mobile_number'],
            password = request.POST['password']
        )

        if user is not None:
            login(request, user)
            if users.is_publish:
                messages.info(request, 'You have succesfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Your account is currently inactive.')
                return redirect('not-active')
        else:
            messages.error(request, 'Mobile Number OR Password is incorrect')
            return redirect('login')
        
    context = {}
    return render(request, 'accounts/login.html', context)

def userRegistration(request):
    userinfoform = UserMemberShipForm()
    userregisterform = CreateUserForm()
    if request.method == 'POST':
        userregisterform = CreateUserForm(request.POST)
        userinfoform = UserMemberShipForm(request.POST)
        if userregisterform.is_valid() & userinfoform.is_valid():
            user = userregisterform.save()
            userinfoform = userinfoform.save(commit=False)
            userinfoform.user = user
            userinfoform.save()

            messages.success(request, 'Account was created for' + " " + user.full_name)
            return redirect('login')
    context = {'userregisterform':userregisterform, 'userinfoform': userinfoform}
    return render(request, 'accounts/user_registration.html', context)

def adminLogin(request):
    if request.method == "POST":
        user = authenticate(
            mobile_number = request.POST['mobile_number'],
            password = request.POST['password']
        )

        if user.is_staff & user.is_superuser is not None:
            login(request, user)
            messages.info(request, 'You have succesfully logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Mobile Number OR Password is incorrect')
            return redirect('admin-login')
        
    context = {}
    return render(request, 'accounts/admin-login.html', context)

def stafRegistration(request):
    form = StafRegistration()
    if request.method == 'POST':
        form = StafRegistration(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'User account was created!')
            return redirect('home')
        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {'form':form}
    return render(request, 'accounts/staf_registration.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def logoutAdmin(request):
    logout(request)
    return redirect('admin-login')