# Generated by Django 3.1.7 on 2021-04-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIDEOSUPLOAD', '0017_auto_20210403_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='thumbnail',
            field=models.TextField(),
        ),
    ]
