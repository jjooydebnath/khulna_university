from django.contrib import admin

from .models import User, UserRegistrationForm, AdminRegister


admin.site.register(User)
admin.site.register(UserRegistrationForm)
admin.site.register(AdminRegister)
