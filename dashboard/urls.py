from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardhome, name="dashboard"),
]
