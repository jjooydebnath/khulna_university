from django.db import models

from accounts.models import User

class CvUpload(models.Model):
    person = models.OneToOneField(User, null=True, blank=True, on_delete= models.CASCADE)
    upload_cv = models.FileField(upload_to='cv', null=True, blank=True)

    def __str__(self):
        return str(self.user.mobile_number)
