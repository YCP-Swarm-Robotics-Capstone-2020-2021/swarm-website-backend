# Generated by Django 2.2.16 on 2020-09-07 02:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('robots', models.ManyToManyField(to='core.Robot')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('log', django.contrib.postgres.fields.jsonb.JSONField()),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Robot')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Run')),
            ],
        ),
    ]