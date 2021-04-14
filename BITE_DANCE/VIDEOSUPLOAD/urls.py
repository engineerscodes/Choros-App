from django.contrib import admin
from django.urls import path
from . import views
from .views import ajaxsubmitVideo

urlpatterns = [
    path('upload/',views.PUTVD,name="UPLOAD"),
    path('videos/',views.allVideos,name="gallery"),
    path('videos/<uuid>',views.getSingleVideo,name="Filter Video"),
    path('',views.homePage,name="HOMEPAGE"),
    path('getcontent/',views.getcontent,name="HOME PAGE VIDEO"),
    path('bitdance/moderator/',views.Moderator,name="Moderator's"),
    path('bitdance/GodMode/',views.GodMode,name="Total Marks"),
    path('bitdance/moderator/ajax',views.ajaxModeration,name="GETMODEAJAX"),
    path('upload/ajax',ajaxsubmitVideo.as_view(),name="upload vidoe"),
    #path('upload/ajax2', views.ajaxsubmitVideo2, name="GET VIDEO"),
    path('getcontent/filter', views.filters, name="DATE FILTER"),
]