# Generated by Django 3.0.5 on 2020-04-28 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apod', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='author',
            new_name='copyright',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='date_photo',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='hd_url_image',
            new_name='hdurl',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='version',
            new_name='service_version',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='url_image',
            new_name='url',
        ),
    ]
