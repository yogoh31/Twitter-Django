# Generated by Django 3.2.6 on 2021-09-02 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
        ('tweets', '0006_auto_20210902_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bigtweet',
            name='tag',
        ),
        migrations.AlterField(
            model_name='bigtweet',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
            preserve_default=False,
        ),
    ]
