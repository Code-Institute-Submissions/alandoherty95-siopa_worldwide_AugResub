# Generated by Django 3.2.6 on 2021-08-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceivedMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email_address', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=254)),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Message',
            },
        ),
    ]