# Generated by Django 3.1.7 on 2021-04-21 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210421_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='content',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
