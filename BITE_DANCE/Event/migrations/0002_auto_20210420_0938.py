# Generated by Django 3.1.7 on 2021-04-20 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventname',
            field=models.CharField(max_length=50),
        ),
    ]