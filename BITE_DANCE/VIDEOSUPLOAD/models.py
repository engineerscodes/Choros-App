from django.db import models
from .VideoSizeVal import file_size
# Create your models here.


class videoUpload(models.Model):
    captions=models.CharField(max_length=100)
    video=models.FileField(upload_to="videos/%y",validators=[file_size])

    def __str__(self):
        return  self.captions








