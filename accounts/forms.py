from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import User, UserRegistrationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'mobile_number', 'password1', 'password2']

        labels = {
            'full_name': 'Full Name',
            'email': 'Email',
            'mobile_number': 'Mobile Number'
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs.update({'class':'form-control', 'placeholder': 'Full Name'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder': 'email@domain.com'})
        self.fields['mobile_number'].widget.attrs.update({'class':'form-control', 'placeholder': '01******'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder': '******'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder': '******'})

class CreateUserInfoForm(ModelForm):
    class Meta:
        model = UserRegistrationForm
        fields = [
            'b_pharm_roll_no', 'm_pharm_roll_no', 'date_of_birth',
            'blood_group', 'name_of_spouse', 'marriage_date', 'no_of_kids',
            'hobbies', 'present_address', 'permanent_address',
            'designation_and_department', 'organization', 'address'
            ]
        
        labels = {
            'b_pharm_roll_no': 'B. Pharm (Roll No.)',
            'm_pharm_roll_no': 'M. Pharm (Roll  No.)',
            'date_of_birth': 'Date of Birth',
            'blood_group' : 'Blood Group',
            'name_of_spouse' : 'Name of Spouse',
            'marriage_date' : 'Marriage Date',
            'no_of_kids' : 'No of Kids',
            'hobbies' : 'Hobbies',
            'present_address' : 'Present Address',
            'permanent_address' : 'Permanent Address',
            'designation_and_department' : 'Designation & Department',
            'organization' : 'Organization',
            'address' : 'Address'
        }


    def __init__(self, *args, **kwargs):
        super(CreateUserInfoForm, self).__init__(*args, **kwargs)

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
        self.fields['address'].widget.attrs.update({'class':'form-control', 'placeholder': ''})