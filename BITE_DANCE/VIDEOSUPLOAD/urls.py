from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.PUTVD,name="UPLOAD"),
    path('videos/',views.allVideos,name="gallery")

]