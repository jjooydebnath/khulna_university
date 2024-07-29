from email.policy import default
from django.db import models

import uuid
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    full_name = models.CharField(max_length=150, null=True)
    email = models.EmailField(unique=True, null=True)
    mobile_number = models.CharField(max_length=11, null=True, unique=True)
    is_publish = models.BooleanField(('publish'), default=False, help_text=(
        'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'))

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['username']

    

    def __str__(self):
        return str(self.mobile_number)
    

def set_username(sender, instance, **kwargs):
    if not instance.username:
        username = instance.full_name
        counter = 1
        while User.objects.filter(username=username):
            username = instance.first_name + str(counter)
            counter += 1
        instance.username = username
models.signals.pre_save.connect(set_username, sender=User)
    
    
    

class UserRegistrationForm(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete= models.SET_NULL)
    b_pharm_roll_no = models.CharField(max_length=100, null=True, blank=True)
    m_pharm_roll_no = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.CharField(max_length=10, null=True, blank=True)
    blood_group = models.CharField(max_length=3, null=True, blank=True)
    name_of_spouse = models.CharField(max_length=150, null=True, blank=True)
    marriage_date = models.CharField(max_length=10, null=True, blank=True)
    no_of_kids = models.IntegerField(null=True, blank=True)
    hobbies = models.CharField(max_length=150, null=True, blank=True)
    present_address = models.CharField(max_length=250, null=True)
    permanent_address = models.CharField(max_length=250, null=True, blank=True)
    designation_and_department = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    

    def __str__(self):
        return str(self.user.mobile_number)
    