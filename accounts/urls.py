from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('login/', views.loginView, name="login"),
    path('user-registration/', views.userRegistration, name="user-registration"),
    path('admin-login/', views.adminLogin, name="admin-login"),
    path('staf-registration/', views.stafRegistration, name="staf-registration"),
    path('payment/', views.paymentInformation, name="payment"),

    path('activate/<str:pk>/', views.activate_user, name='activate_user'),
    path('deactivate/<str:pk>/', views.deactivate_user, name='deactivate_user'),

    path('logout/', views.logoutUser, name="logout"),
    path('logout-admin/', views.logoutAdmin, name="logout-admin"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),

]
