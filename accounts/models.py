from email.policy import default
from django.db import models

import uuid
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    full_name = models.CharField(max_length=150, null=True)
    email = models.EmailField(unique=True, null=True)
    mobile_number = models.CharField(max_length=11, null=True, unique=True)

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.mobile_number)
    

class UserRegistrationForm(models.Model):
    b_pharm_roll_no = models.CharField(max_length=100, null=True, blank=True)
    m_pharm_roll_no = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3, null=True, blank=True)
    name_of_spouse = models.CharField(max_length=150, null=True, blank=True)
    marriage_date = models.DateField()
    no_of_kids = models.IntegerField(null=True, blank=True)
    hobbies = models.CharField(max_length=150, null=True, blank=True)
    Present_address = models.CharField(max_length=250, null=True)
    permanent_address = models.CharField(max_length=250, null=True, blank=True)
    designation_and_department = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.user.name)
    