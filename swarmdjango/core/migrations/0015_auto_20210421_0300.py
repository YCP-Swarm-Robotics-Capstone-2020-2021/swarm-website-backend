# Generated by Django 3.1.7 on 2021-04-21 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_run'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='log',
        ),
        migrations.RemoveField(
            model_name='run',
            name='run',
        ),
        migrations.AddField(
            model_name='run',
            name='filePath',
            field=models.TextField(default='NotSet'),
        ),
    ]