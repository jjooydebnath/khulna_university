from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import User, UserRegistrationForm
from accounts.forms import CreateUserForm, UserMemberShipForm

from .forms import ProfileInfoEdit, UserCvUploadForm


@login_required(login_url='login')
def userHome(request):
    return render(request, 'userprofile/user_home.html')

@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    userinfo = user.userregistrationform
    context = {'user': user, 'users': userinfo}
    return render(request, 'userprofile/user_profile.html', context)

@login_required(login_url='login')
def editUserProfile(request):
    user = request.user
    form = CreateUserForm(instance=user)
    addform = UserMemberShipForm(instance=user.userregistrationform)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES, instance=user)
        addform = UserMemberShipForm(request.POST, instance=user.userregistrationform)
        if form.is_valid() & addform.is_valid():
            form.save()
            addform.save()
            return redirect('user-home')
        
        else:
            form = CreateUserForm(instance=user)
            addform = UserMemberShipForm(instance=user.userregistrationform)

    context = {'form': form, 'addform':addform}
    return render(request, 'userprofile/edit_user_profile.html', context)

def cvUpload(request):
    user = request.user
    form = UserCVUploadForm()
    if request.method == "POST":
        form = UserCvUploadForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render (request, 'userprofile/cv_upload.html', context)