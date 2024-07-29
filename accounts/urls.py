from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.loginView, name="login"),
    path('user-registration/', views.userRegistration, name="user-registration"),
    path('admin-login/', views.adminLogin, name="admin-login"),
    path('staf-registration/', views.stafRegistration, name="staf-registration"),

    path('logout/', views.logoutEveryBody, name="logout"),

]
