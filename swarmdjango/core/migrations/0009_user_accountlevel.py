# Generated by Django 2.2.16 on 2020-10-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_merge_20201008_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accountLevel',
            field=models.IntegerField(default=0),
        ),
    ]
