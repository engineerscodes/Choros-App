from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('upload/',views.PUTVD,name="UPLOAD"),
    path('videos/',views.allVideos,name="gallery"),
    path('videos/<uuid>',views.getSingleVideo,name="Filter Video"),
    path('',views.homePage,name="HOMEPAGE"),
    path('bitdance/moderator/',views.Moderator,name="Moderator's"),
    path('bitdance/GodMode/',views.GodMode,name="Total Marks")

]