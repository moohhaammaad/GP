# Generated by Django 2.0.2 on 2018-04-06 12:23

from django.db import migrations, models

import dashboard.models.utilities


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0012_auto_20180406_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='account',
            name='logo',
            field=models.FileField(default='hi', upload_to=dashboard.models.utilities.get_path_with_time_now),
            preserve_default=False,
        ),
    ]