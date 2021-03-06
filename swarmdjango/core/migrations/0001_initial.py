# Generated by Django 2.2.15 on 2020-08-31 22:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('context', models.TextField()),
                ('textAdded', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('replies', models.ManyToManyField(related_name='_comment_replies_+', to='core.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('description', models.TextField()),
                ('fileName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('comments', models.ManyToManyField(to='core.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageType', models.TextField()),
                ('pageTitle', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.User')),
                ('receiveUpdates', models.BooleanField()),
            ],
            bases=('core.user',),
        ),
        migrations.CreateModel(
            name='SponsorPersonalPage',
            fields=[
                ('personalpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.PersonalPage')),
                ('missionStatement', models.TextField()),
                ('reasonForSponsorship', models.TextField()),
                ('companyLink', models.URLField()),
            ],
            bases=('core.personalpage',),
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('briefDescription', models.TextField()),
                ('entries', models.ManyToManyField(to='core.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.TextField()),
                ('caption', models.TextField()),
                ('uploadedBy', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
        ),
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('log', models.ManyToManyField(to='core.Change')),
                ('subHeadings', models.ManyToManyField(related_name='_heading_subHeadings_+', to='core.Heading')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='contributors',
            field=models.ManyToManyField(to='core.User'),
        ),
        migrations.AddField(
            model_name='entry',
            name='headings',
            field=models.ManyToManyField(to='core.Heading'),
        ),
        migrations.AddField(
            model_name='entry',
            name='log',
            field=models.ManyToManyField(to='core.Change'),
        ),
        migrations.AddField(
            model_name='entry',
            name='sideBar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.SideBar'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.User'),
        ),
        migrations.AddField(
            model_name='change',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.User'),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.User')),
                ('companyName', models.TextField()),
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.PersonalPage')),
            ],
            bases=('core.user',),
        ),
        migrations.CreateModel(
            name='DevPersonalPage',
            fields=[
                ('personalpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.PersonalPage')),
                ('expectedGraduationYear', models.IntegerField()),
                ('biography', models.TextField()),
                ('motivationForWorking', models.TextField()),
                ('contributions', models.ManyToManyField(to='core.Contribution')),
            ],
            bases=('core.personalpage',),
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.User')),
                ('teamRole', models.TextField()),
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.PersonalPage')),
            ],
            bases=('core.user',),
        ),
    ]
