from rest_framework import serializers
from .models import videoUpload,Marks

class MarksSerializer(serializers.ModelSerializer) :
    class Meta:
        model=Marks
        #fields="__all__"
        fields=('video_link','date','by_email')

class videoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model= videoUpload
        #fields="__all__"
        fields=('url_64encoding','date','username')