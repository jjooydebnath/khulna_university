from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('not-active/', views.notActiveUser, name="not-active"),
]
