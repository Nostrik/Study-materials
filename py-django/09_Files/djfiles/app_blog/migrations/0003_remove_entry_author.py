# Generated by Django 2.2 on 2022-03-31 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_auto_20220331_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
    ]