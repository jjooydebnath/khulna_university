from django.shortcuts import render

from accounts.models import User, UserRegistrationForm
from accounts.forms import CreateUserForm, UserCreationForm

def userHome(request):
    return render(request, 'userprofile/user_home.html')

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    userinfo = UserRegistrationForm.objects.all(instance=user)
    context = {'user': user, 'users': userinfo}
    return render(request, 'userprofile/user_profile.html', context)

def editUserProfile(request):
    user = request.user
    form = CreateUserForm(instance=user)
    addform = UserCreationForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES, instance=user)
        addform = UserCreationForm(request.POST, instance=user)
        if form.is_valid() & addform.is_valid():
            form.save()
            addfrom.save()
    context = {'form': form, 'addform':addform}
    return render(request, 'userprofile/edit_user_profile.html')