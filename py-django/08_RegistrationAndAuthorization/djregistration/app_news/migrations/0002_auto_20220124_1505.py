# Generated by Django 2.2 on 2022-01-24 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_news.News', verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default='', max_length=1000, verbose_name='Текст комментария'),
        ),
    ]
