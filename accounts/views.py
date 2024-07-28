from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import CreateUserForm, CreateUserInfoForm
from .models import User, UserRegistrationForm


def loginView(request):
    if request.method == "POST":
        user = authenticate(
            mobile_number = request.POST['mobile_number'],
            password = request.POST['password']
        )

        if user is not None:
            login(request, user)
            if user.is_active:
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
    userregisterform = CreateUserForm()
    userinfoform = CreateUserInfoForm()
    if request.method == 'POST':
        userregisterform = CreateUserForm(request.POST)
        userinfoform = CreateUserInfoForm(request.POST)
        if userregisterform.is_valid() & userinfoform.is_valid():
            user = userregisterform.save()
            userinfoform = userinfoform.save(False)
            userinfoform.user = user
            userinfoform.save()

            messages.success(request, 'Account was created for' + " " + user.full_name)
            return redirect('login')
    context = {'userregisterform':userregisterform, 'userinfoform': userinfoform}
    return render(request, 'accounts/user_registration.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')