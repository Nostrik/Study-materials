<<<<<<< HEAD
# Generated by Django 2.2 on 2022-01-16 19:58

from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 2.2 on 2022-01-17 11:17

from django.db import migrations, models
>>>>>>> 607e9a076908c872ae1ed29f0417674ca6882240


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='AdvertisementStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> 607e9a076908c872ae1ed29f0417674ca6882240
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=1500, verbose_name='Заголовок')),
                ('description', models.TextField(default='', max_length=1000, verbose_name='описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField(default=0, verbose_name='цена')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
<<<<<<< HEAD
                ('status', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisement', to='advertisements_app.AdvertisementStatus', verbose_name='статус')),
=======
>>>>>>> 607e9a076908c872ae1ed29f0417674ca6882240
            ],
            options={
                'db_table': 'advertisement',
                'ordering': ['title'],
            },
        ),
    ]
