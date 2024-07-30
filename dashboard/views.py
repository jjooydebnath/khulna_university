from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm
from accounts.models import User, UserRegistrationForm

def dashboardhome(request):
    user = request.user
    users = UserRegistrationForm.objects.all()
    if user.is_staff or user.is_superuser:
        # usercount = users.count
        activecount = users.filter(is_publish=True).count()
        dactivecount = users.filter(is_publish=False).count()
        context = {'users': users, 'activecount': activecount, 'dactivecount': dactivecount}
        return render(request, 'dashboard/dashboard_home.html', context)
    else:
        return render(request, 'dashboard/not_authrized.html')
    
def userEdit(request, pk):
    user = request.user
    userobj = User.objects.get(id=pk)
    userformobj = CreateUserInfoForm(instance=userobj)
    if user.is_staff or user.is_superuser:
        if request.method == 'POST':
            userformobj = CreateUserInfoForm(request.POST, instance=userobj, id=pk)
            if userformobj.is_valid():
                userformobj.save()
                return redirect('dashboard')
        context = {'userobj': userobj, 'userformobj': userformobj}
        return render(request, 'dashboard/user_edit_page.html', context)
    else:
        return render(request, 'dashboard/not_authrized.html')
    