# Generated by Django 3.0.3 on 2020-03-31 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='publish',
        ),
    ]
