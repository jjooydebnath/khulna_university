from django.shortcuts import render
from accounts.models import User

def dashboardhome(request):
    user = request.user
    if user.is_staff or user.is_superuser:
        return render(request, 'dashboard/dashboard_home.html')
    else:
        return render(request, 'dashboard/not_authrized.html')