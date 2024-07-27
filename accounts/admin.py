from django.contrib import admin

from .models import User, UserRegistrationForm


admin.site.register(User)
admin.site.register(UserRegistrationForm)
