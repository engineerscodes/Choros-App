from django.db import models
from .VideoSizeVal import file_size
from django.core.validators import FileExtensionValidator
# Create your models here.


class videoUpload(models.Model):

    captions=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    date=models.DateField(default='2001-04-12')
    thumbnail=models.URLField()
    video=models.FileField(upload_to="videos/%y",validators=[file_size,FileExtensionValidator(allowed_extensions=['mp4','MOV','MKV'])])
    url_64encoding=models.CharField(max_length=2048,default='/upload/videos/')
    def __str__(self):
        return  self.captions


class Marks(models.Model):
    videoId=models.CharField(max_length=250)
    by_email=models.CharField(max_length=250)
    marks=models.IntegerField()
    moderator_email=models.CharField(max_length=250)
    video_link=models.URLField()
    date=models.DateField(default='2001-04-12')
    verfiyed=models.BooleanField(default=False)
    def __str__(self):
        return "VideoID:" +self.video_link+" BY :"+self.moderator_email









