# Generated by Django 3.2.6 on 2021-08-18 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='content_image_1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='content_image_2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='content_image_url_1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='content_image_url_2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='title_image',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='title_image_url_1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='updated_at',
        ),
    ]
