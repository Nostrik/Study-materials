# Generated by Django 2.2 on 2022-02-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0006_auto_20220203_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='administration',
            field=models.CharField(choices=[('d', 'Удалено администратором')], default='', max_length=30, verbose_name='Администрирование'),
        ),
    ]