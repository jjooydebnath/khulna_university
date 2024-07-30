from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardhome, name="dashboard"),
    path('user-edit/<str:pk>/', views.userEdit, name="user-edit"),
]
