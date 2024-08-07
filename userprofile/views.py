from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# import io
# import xhtml2pdf.pisa as pisa
# from django.template.loader import get_template

from accounts.models import User, UserRegistrationForm
from accounts.forms import CreateUserForm, UserMemberShipForm

from .forms import ProfileInfoEdit, AddProfileEdit, UserCvUploadForm


@login_required(login_url='login')
def userHome(request):
    user =  request.user
    if user.userregistrationform.is_publish is True:

        return render(request, 'userprofile/user_home.html')
    else:
        return render(request, 'base/not-active.html')

@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    userinfo = user.userregistrationform
    if user.userregistrationform.is_publish is True:
        context = {'user': user, 'users': userinfo}
        return render(request, 'userprofile/user_profile.html', context)
    else:
        return render(request, 'base/not-active.html')

@login_required(login_url='login')
def editUserProfile(request):
    user = request.user
    form = ProfileInfoEdit(instance=user)
    addform = AddProfileEdit(instance=user.userregistrationform)
    if user.userregistrationform.is_publish is True:
        if request.method == 'POST':
            form = ProfileInfoEdit(request.POST, request.FILES, instance=user)
            addform = AddProfileEdit(request.POST, instance=user.userregistrationform)
            if form.is_valid() & addform.is_valid():
                form.save()
                addform.save()
                return redirect('user-home')
            
            else:
                form = ProfileInfoEdit(instance=user)
                addform = AddProfileEdit(instance=user.userregistrationform)

        context = {'form': form, 'addform':addform}
        return render(request, 'userprofile/edit_user_profile.html', context)
    else:
        return render(request, 'base/not-active.html')

@login_required(login_url='login')
def cvUpload(request):
    user = request.user
    form = UserCvUploadForm(request.POST, request.FILES)
    if user.userregistrationform.is_publish is True:
        if request.method == "POST":
            form = UserCvUploadForm(request.POST, request.FILES)
            if form.is_valid():
                cv_upload = form.save(commit=False)
                cv_upload.person = user
                cv_upload.save()
                messages.info(request, 'File Uploaded')
                return redirect('user-home')
            else:
                form = UserCvUploadForm()
                messages.error(request, 'File not uploaded')
        context = {'form': form}
        return render (request, 'userprofile/cv_upload.html', context)
    else:
        return render(request, 'base/not-active.html')


# def generate_pdf(request, pk):
#     user = request.user
#     users = User.objects.get(id=pk)
#     otherinfo = UserRegistrationForm.objects.get(instance=users)
#     context ={
#         'users': users,
#         'otherinfo' : otherinfo
#     }
#     template_path = 'userprofile/profile_pdf.html'  # Replace with your template path
#     template = get_template(template_path)
#     html = template.render(context)
#     response = io.BytesIO()
#     pdf = pisa.CreatePDF(html, dest=response)