# Generated by Django 2.2.16 on 2020-10-01 01:50

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200909_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='content',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
    ]