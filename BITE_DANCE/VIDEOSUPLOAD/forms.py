
from django import forms
from .models import videoUpload

class vd_form(forms.ModelForm):
    class Meta :
        model=videoUpload
        fields=("captions","video")