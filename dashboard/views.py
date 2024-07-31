from django.shortcuts import render, redirect
from accounts.forms import CreateUserForm, UserMemberShipForm
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
        return render(request, 'dashboard/user_edit_page.html', context)
    else:
        return render(request, 'dashboard/not_authrized.html')