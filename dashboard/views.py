from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404

from accounts.forms import CreateUserForm, UserMemberShipForm, AddRegisterForm, PaymentInformationForm
from accounts.models import User, UserRegistrationForm, AdminRegister, PaymentInformation

def dashboardhome(request):
    user = request.user
    users = UserRegistrationForm.objects.all()
    admins = AdminRegister.objects.all()
    if user.is_staff or user.is_superuser:
        # usercount = users.count
        activecount = users.filter(is_publish=True).count()
        dactivecount = users.filter(is_publish=False).count()
        admincount = admins.filter().count()
        context = {'users': users, 'activecount': activecount, 
                   'dactivecount': dactivecount, 'admincount': admincount
                   }
        return render(request, 'dashboard/dashboard_home.html', context)
    else:
        return render(request, 'dashboard/not_authrized.html')
    
def adminUserInfo(request, pk):
    user = request.user
    userinfo = User.objects.get(id=pk)
    if user.is_staff or user.is_superuser:
        users = User.objects.get(id=pk)
        useradd = users.userregistrationform

        if request.method == 'POST':
            useradd_data = UserMemberShipForm(request.POST, instance=useradd)
            if useradd_data.is_valid():
                useradd_data.save()
                return redirect('dashboard')
        else:
            useradd_data = UserMemberShipForm(instance=useradd)
        context = {'useradd_data': useradd_data, 'userinfo': userinfo}
        return render(request, 'dashboard/user_info.html', context)
    else:
        return render(request, 'dashboard/not_authrized.html')
    

def paymentInfo(request, pk):
    user = request.user
    users = User.objects.get(id=pk)
    payinfo = PaymentInformation.objects.all()
    if user.is_staff or user.is_superuser:
        context = {'users': users, 'payinfo': payinfo}
        return render(request, 'dashboard/payment_info.html', context)
    else:
        return render(request, 'dashboard/not_authrized.html')
    
def adminList(request):
    user = request.user
    admins = AdminRegister.objects.all()
    
    if user.is_staff or user.is_superuser:
        context = {'admins': admins}
        return render(request, 'dashboard/admin_list.html', context)
    else:
        return render(request, 'dashboard/not_authrized.html')
    
def send_email(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':

        # Create the email subject and message
        subject = request.POST['subject']
        message = request.POST['message']
        
        # Send the email
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return redirect('admin-list')
    return render(request, 'dashboard/email_sent.html')