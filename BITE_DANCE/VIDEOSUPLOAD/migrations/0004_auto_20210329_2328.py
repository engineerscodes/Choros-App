# Generated by Django 3.1.7 on 2021-03-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIDEOSUPLOAD', '0003_videoupload_url_64encoding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]