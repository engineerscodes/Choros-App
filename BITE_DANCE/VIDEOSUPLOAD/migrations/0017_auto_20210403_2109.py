# Generated by Django 3.1.7 on 2021-04-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIDEOSUPLOAD', '0016_auto_20210403_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='thumbnail',
            field=models.TextField(editable=False),
        ),
    ]
