# Generated by Django 3.2.6 on 2021-08-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]