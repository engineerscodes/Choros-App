# Generated by Django 3.1.7 on 2021-04-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moderator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mode',
            name='username',
            field=models.CharField(default='', max_length=250),
        ),
    ]