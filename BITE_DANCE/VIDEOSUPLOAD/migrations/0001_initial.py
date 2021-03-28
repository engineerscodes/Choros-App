# Generated by Django 3.1.7 on 2021-03-28 19:11

import VIDEOSUPLOAD.VideoSizeVal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videoUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captions', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos/%y', validators=[VIDEOSUPLOAD.VideoSizeVal.file_size, django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'AVI', 'MKV'])])),
            ],
        ),
    ]
