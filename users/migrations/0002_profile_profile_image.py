# Generated by Django 3.2.6 on 2021-08-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='get_upload_path'),
        ),
    ]
