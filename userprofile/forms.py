from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from accounts.models import User, UserRegistrationForm
from .models import CvUpload

class ProfileInfoEdit(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'mobile_number', 'profile_picture']


class UserCvUploadForm(ModelForm):
    class Meta:
        fields = ['upload_cv']