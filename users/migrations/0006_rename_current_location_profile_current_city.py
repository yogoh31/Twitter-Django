# Generated by Django 3.2.6 on 2021-08-31 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_current_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='current_location',
            new_name='current_city',
        ),
    ]
