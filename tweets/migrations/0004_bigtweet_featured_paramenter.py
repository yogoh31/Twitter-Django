# Generated by Django 3.2.6 on 2021-09-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_bigtweet_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigtweet',
            name='featured_paramenter',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
