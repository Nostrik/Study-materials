# Generated by Django 2.2 on 2022-04-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0009_auto_20220411_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='photo',
        ),
        migrations.AddField(
            model_name='picture',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]