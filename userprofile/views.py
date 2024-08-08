from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import os
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 


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

def profile_pdf(request, pk):
    # Retrieve user profile data
    user =  User.objects.get(id=pk)
    user_profile = user.userregistrationform

    # Create context for the template
    context = {
        'full_name': user.full_name,
        'email': user.email,
        'mobile_number': user.mobile_number,
        'profile_picture': user.profile_picture,
        'b_pharm_roll_no': user_profile.b_pharm_roll_no,
        'm_pharm_roll_no': user_profile.m_pharm_roll_no,
        'date_of_birth': user_profile.date_of_birth,
        'blood_group': user_profile.blood_group,
        'name_of_spouse': user_profile.name_of_spouse,
        'marriage_date': user_profile.marriage_date,
        'no_of_kids': user_profile.no_of_kids,
        'hobbies': user_profile.hobbies,
        'present_address': user_profile.present_address,
        'permanent_address': user_profile.permanent_address,
        'designation_and_department': user_profile.designation_and_department,
        'organization': user_profile.organization,
        'organization_address': user_profile.organization_address,
        'membership_status': user_profile.membership_status,

    }

    # Render the template to HTML
    template_path = 'userprofile/profile_pdf.html'
    html = render(request, template_path, context).content.decode('utf-8')

    # Create a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="profile.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response 