from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task


from .forms import CreateUserForm, UserMemberShipForm, StafRegistration, AddRegisterForm, PaymentInformationForm
from .models import User, UserRegistrationForm, PaymentInformation, AdminRegister
from .decorators import unauthenticated_user

@unauthenticated_user
def loginView(request):
    if request.method == "POST":
        user = authenticate(
            mobile_number = request.POST['mobile_number'],
            password = request.POST['password']
        )

        if user is not None:
            login(request, user)
            if user.userregistrationform.is_publish:
                messages.info(request, 'You have succesfully logged in.')
                return redirect('user-home')
            else:
                messages.error(request, 'Your account is currently inactive.')
                return redirect('not-active')
        else:
            messages.error(request, 'Mobile Number OR Password is incorrect')
            return redirect('login')
        
    context = {}
    return render(request, 'accounts/login.html', context)

@unauthenticated_user
def userRegistration(request):
    userinfoform = UserMemberShipForm()
    userregisterform = CreateUserForm()
    if request.method == 'POST':
        userregisterform = CreateUserForm(request.POST, request.FILES)
        userinfoform = UserMemberShipForm(request.POST)
        if userregisterform.is_valid() & userinfoform.is_valid():
            user = userregisterform.save()
            userinfoform = userinfoform.save(commit=False)
            userinfoform.user = user
            userinfoform.save()

            users = AdminRegister.objects.filter(is_publish=True)
            subject = f'New User Registered: {user.full_name}'
            message = f'''Dear Sir/Madam,\n 
            A new User is Created please Check.\n
            Full Name: {user.full_name}\n
            Mobile Number: {user.mobile_number}\n
            Email: {user.email}\n
            Membership Status: {user.userregistrationform.membership_status}
            '''
            for adminemail in users:
                admin_email = adminemail.user.email
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])

            messages.success(request, 'Account was created for' + " " + user.full_name)
            return redirect('login')
    context = {'userregisterform':userregisterform, 'userinfoform': userinfoform}
    return render(request, 'accounts/user_registration.html', context)

@unauthenticated_user
def adminLogin(request):
    if request.method == "POST":
        user = authenticate(
            mobile_number = request.POST['mobile_number'],
            password = request.POST['password']
        )

        if user.is_staff & user.is_superuser is not None:
            login(request, user)
            if user.adminregister.is_publish:
                messages.info(request, 'You have succesfully logged in.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Your account is currently inactive.')
                return redirect('not-active')
        else:
            messages.error(request, 'Mobile Number OR Password is incorrect')
            return redirect('admin-login')
        
    context = {}
    return render(request, 'accounts/admin-login.html', context)

def stafRegistration(request):
    form = StafRegistration()
    addform = AddRegisterForm()
    if request.method == 'POST':
        form = StafRegistration(request.POST)
        addform = AddRegisterForm(request.POST)
        if form.is_valid() & addform.is_valid():
            user = form.save()
            addform = addform.save(commit=False)
            addform.user = user
            addform.save()

            messages.success(request, 'User account was created!')
            return redirect('dashboard')
        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {'form':form, 'addform':addform}
    return render(request, 'accounts/staf_registration.html', context)

def paymentInformation(request):
    user = request.user
    form = PaymentInformationForm(request.POST)
    if request.method == "POST":
        form = PaymentInformationForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.person = user
            forms.save()
            messages.info(request, 'successfully Information update')
            return redirect('user-home')
    context = {'form': form}
    return render(request, 'accounts/payment_information.html', context)

def activate_user(request, pk):
    user = get_object_or_404(UserRegistrationForm, id=pk)
    user.is_publish = True
    user.last_activated = timezone.now()
    user.save()
    return redirect('dashboard')

def deactivate_user(request, pk):
    user = get_object_or_404(UserRegistrationForm, id=pk)
    user.is_publish = False
    user.save()
    return redirect('dashboard')


# Set the time limit for the active status
ACTIVE_DURATION = timedelta(hours=1)
@shared_task
def auto_deactivate_users():
    # Automatically deactivate users whose active period has expired
    expired_users = UserRegistrationForm.objects.filter(is_publish=True, last_activated__lte=timezone.now() - ACTIVE_DURATION)
    expired_users.update(is_publish=False)


def logoutUser(request):
    logout(request)
    return redirect('login')


def logoutAdmin(request):
    logout(request)
    return redirect('admin-login')