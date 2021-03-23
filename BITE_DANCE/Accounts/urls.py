from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('reg/',views.reg,name="REG"),
    path('activate/<uidb64>/<token>',views.AUTHUSERNAME,name="activate")
]