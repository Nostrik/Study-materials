# Generated by Django 2.2 on 2022-02-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0009_auto_20220218_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='administration',
            field=models.CharField(choices=[('d', 'Удалено администратором')], default=None, max_length=30, verbose_name='Администрирование'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(db_index=True, default=None, max_length=1500, null=True, verbose_name='Имя пользователя'),
        ),
    ]
