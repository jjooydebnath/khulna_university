from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from accounts.models import User, UserRegistrationForm
from .models import CvUpload

class ProfileInfoEdit(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'mobile_number', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(ProfileInfoEdit, self).__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs.update({'class':'form-control', 'placeholder': 'Full Name'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder': 'email@domain.com'})
        self.fields['mobile_number'].widget.attrs.update({'class':'form-control', 'placeholder': '01******'})
        self.fields['profile_picture'].widget.attrs.update({'class':'form-control', 'placeholder': ''})

class AddProfileEdit(ModelForm):
    class Meta:
        model = UserRegistrationForm
        fields = [
            'b_pharm_roll_no', 'm_pharm_roll_no', 'date_of_birth', 'blood_group',
            'name_of_spouse', 'marriage_date', 'no_of_kids', 'hobbies', 'present_address', 'permanent_address',
            'designation_and_department', 'organization', 'organization_address'
        ]

    def __init__(self, *args, **kwargs):
        super(AddProfileEdit, self).__init__(*args, **kwargs)

        self.fields['b_pharm_roll_no'].widget.attrs.update({'class':'form-control', 'placeholder': 'e.g 1***'})
        self.fields['m_pharm_roll_no'].widget.attrs.update({'class':'form-control', 'placeholder': 'e.g 1***'})
        self.fields['date_of_birth'].widget.attrs.update({'class':'form-control', 'placeholder': 'DD/MM/YYYY'})
        self.fields['blood_group'].widget.attrs.update({'class':'form-control', 'placeholder': 'AB+'})
        self.fields['name_of_spouse'].widget.attrs.update({'class':'form-control', 'placeholder': 'Name of Wife'})
        self.fields['marriage_date'].widget.attrs.update({'class':'form-control', 'placeholder': 'DD/MM/YYYY'})
        self.fields['no_of_kids'].widget.attrs.update({'class':'form-control', 'placeholder': ''})
        self.fields['hobbies'].widget.attrs.update({'class':'form-control', 'placeholder': ''})
        self.fields['present_address'].widget.attrs.update({'class':'form-control', 'placeholder': ''})
        self.fields['permanent_address'].widget.attrs.update({'class':'form-control', 'placeholder': ''})
        self.fields['designation_and_department'].widget.attrs.update({'class':'form-control', 'placeholder': ''})
        self.fields['organization'].widget.attrs.update({'class':'form-control', 'placeholder': ''})
        self.fields['organization_address'].widget.attrs.update({'class':'form-control', 'placeholder': ''})


class UserCvUploadForm(ModelForm):
    class Meta:
        model = CvUpload
        fields = ['upload_cv']

