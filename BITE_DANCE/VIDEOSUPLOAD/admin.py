from django.contrib import admin
from .models import videoUpload,Marks
# Register your models here.

class adminvideoDetails(admin.ModelAdmin):
    list_display=('username','Total_marks','date')
    search_fields = ('username','date','captions')
    list_filter = ('username','date',)

class MarksDetails(admin.ModelAdmin):
    list_display = ('videoId','by_email','marks','moderator_email','date')
    search_fields = ('videoId','by_email','marks','moderator_email','date')
    list_filter = ('by_email','moderator_email','date')

admin.site.register(videoUpload,adminvideoDetails)
admin.site.register(Marks,MarksDetails)