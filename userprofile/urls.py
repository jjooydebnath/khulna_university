from django.urls import path

from .import views
urlpatterns = [
    path('', views.userHome, name="user-home"),
    path('user-profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('edit-user-profile/', views.editUserProfile, name="edit-user-profile"),
    path('cv-upload/', views.cvUpload, name="cv-upload"),
    path('profile-pdf/<str:pk>/', views.profile_pdf, name="profile-pdf"),
]
