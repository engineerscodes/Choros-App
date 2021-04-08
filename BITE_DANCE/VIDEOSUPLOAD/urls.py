from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('upload/', views.PUTVD, name="UPLOAD"),
    path('videos/', views.allVideos, name="gallery"),
    path('videos/<uuid>', views.getSingleVideo, name="Filter Video"),
    path('', views.homePage, name="HOMEPAGE"),
    path('bitdance/moderator/', views.Moderator, name="Moderator's"),
    path('bitdance/GodMode/', views.GodMode, name="Total Marks")
=======
    path('upload/',views.PUTVD,name="UPLOAD"),
    path('videos/',views.allVideos,name="gallery"),
    path('videos/<uuid>',views.getSingleVideo,name="Filter Video"),
    path('',views.homePage,name="HOMEPAGE"),
    path('bitdance/moderator/',views.Moderator,name="Moderator's"),
    path('bitdance/GodMode/',views.GodMode,name="Total Marks"),
    path('bitdance/moderator/ajax',views.ajaxModeration,name="GETMODEAJAX")
>>>>>>> f42d09f923615e65a7ae232f0c36e8108a86e418

]
