# Generated by Django 2.2 on 2022-03-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0013_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]