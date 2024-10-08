from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardhome, name="dashboard"),
    path('admin-user-info/<str:pk>/', views.adminUserInfo, name="admin-user-info"),
    path('payment-info/<str:pk>/', views.paymentInfo, name="payment-info"),
    path('admin-list/', views.adminList, name="admin-list"),

    path('send-mail/<str:pk>/', views.send_email, name="send-mail"),


]
