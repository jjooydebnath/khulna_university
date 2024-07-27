from django.shortcuts import render


def loginView(request):
    return render(request, 'accounts/login.html')