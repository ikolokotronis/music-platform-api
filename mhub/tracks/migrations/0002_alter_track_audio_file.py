# Generated by Django 4.0.3 on 2022-04-04 13:11

from django.db import migrations, models
import tracks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='audio_file',
            field=models.FileField(upload_to=tracks.models.upload_location),
        ),
    ]
