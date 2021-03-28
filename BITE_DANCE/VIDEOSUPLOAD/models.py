from django.db import models
from .VideoSizeVal import file_size
from django.core.validators import FileExtensionValidator
# Create your models here.


class videoUpload(models.Model):
    captions=models.CharField(max_length=100)
    username=models.CharField(max_length=100)

    video=models.FileField(upload_to="videos/%y",validators=[file_size,FileExtensionValidator(allowed_extensions=['mp4','MOV','AVI','MKV'])])

    def __str__(self):
        return  self.captions








