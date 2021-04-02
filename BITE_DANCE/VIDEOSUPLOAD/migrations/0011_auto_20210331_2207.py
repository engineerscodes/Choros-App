# Generated by Django 3.1.7 on 2021-03-31 16:37

import VIDEOSUPLOAD.VideoSizeVal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIDEOSUPLOAD', '0010_auto_20210331_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoId', models.CharField(max_length=250)),
                ('by_email', models.CharField(max_length=250)),
                ('marks', models.IntegerField()),
                ('moderator_email', models.CharField(max_length=250)),
                ('video_link', models.URLField()),
                ('date', models.DateField(default='2001-04-12')),
                ('verfiyed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='videoupload',
            name='video',
            field=models.FileField(upload_to='videos/%y', validators=[VIDEOSUPLOAD.VideoSizeVal.file_size, django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'MKV'])]),
        ),
    ]
