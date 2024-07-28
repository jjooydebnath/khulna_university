from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.loginView, name="login"),
    path('user-registration/', views.userRegistration, name="user-registration"),

]
