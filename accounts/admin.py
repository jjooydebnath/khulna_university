from django.contrib import admin

from .models import User, UserRegistrationForm, AdminRegister, PaymentInformation


admin.site.register(User)
admin.site.register(UserRegistrationForm)
admin.site.register(AdminRegister)
admin.site.register(PaymentInformation)
