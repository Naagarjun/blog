# Generated by Django 3.0.3 on 2020-02-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=255),
        ),
    ]
