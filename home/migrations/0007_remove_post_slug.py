# Generated by Django 3.0.3 on 2020-03-01 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
