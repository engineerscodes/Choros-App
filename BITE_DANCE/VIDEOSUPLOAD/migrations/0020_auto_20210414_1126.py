# Generated by Django 3.2 on 2021-04-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIDEOSUPLOAD', '0019_auto_20210403_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='video_link',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='videoupload',
            name='thumbnail',
            field=models.TextField(),
        ),
    ]