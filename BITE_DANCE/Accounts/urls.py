from os import name
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Account management
    path('login/', views.login, name="login"),
    path('reg/', views.reg, name="REG"),
    path('logout/', views.logout, name="LOGOUT"),
    path('activate/<uidb64>/<token>', views.AUTHUSERNAME, name="activate"),

    # Password management
    # - forgot password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="Password/password_reset.html"),
         name="password_reset"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="Password/password_reset_done.html"),
         name="password_reset_done"),

    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="Password/password_reset_confirm.html"), name="password_reset_confirm"),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="Password/password_reset_complete.html"), name="password_reset_complete"),

    # - change password
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="Password/password_change.html"),
         name="password_change"),

    path('password_change/done/ ',
         auth_views.PasswordChangeDoneView.as_view(), name='password_change_done')

]
