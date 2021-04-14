from os import name
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('reg/', views.reg, name="REG"),
    path('logout/', views.logout, name="LOGOUT"),
    path('activate/<uidb64>/<token>', views.AUTHUSERNAME, name="activate"),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name="password_reset"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")

]
