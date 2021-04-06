from rest_framework import serializers
from .models import videoUpload,Marks

class MarksSerializer(serializers.ModelSerializer) :
    class Meta:
        model=Marks
        fields="__all__"

class videoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model= videoUpload
        fields="__all__"