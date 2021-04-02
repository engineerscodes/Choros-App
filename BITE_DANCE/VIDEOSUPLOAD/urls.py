from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.PUTVD,name="UPLOAD"),
    path('videos/',views.allVideos,name="gallery"),
    path('videos/<uuid>',views.getSingleVideo,name="Filter Video"),
    path('HomePage/',views.homePage,name="HOMEPAGE"),
    path('moderator/<uuid>',views.Moderator,name="Moderator's")

]