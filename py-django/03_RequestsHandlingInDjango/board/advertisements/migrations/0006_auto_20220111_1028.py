# Generated by Django 2.2 on 2022-01-11 07:28

from django.db import migrations
import datetime
import random


def gen_advertisement(apps, schema_editor):
    title_list = ['Личные вещи', 'Транспорт', 'Работа', 'Запчасти и аксессуары', 'Для дома и дачи', 'Недвижимость',
                  'Предложение услуг', 'Хобби и отдых', 'Электроника', 'Животные', 'Готовый бизнес и оборудование']
    sample_description = 'тестовое описание тестового объявления'
    Advertisement = apps.get_model('advertisements', 'Advertisement')
    Advertisement.objects.create(title='Тест объявление 1', description='тестовое объявление номер 1')
    Advertisement.objects.create(title='Тест объявление 2', description='тестовое объявление номер 2')
    Advertisement.objects.create(title='Тест объявление 3', description='тестовое объявление номер 3')
    Advertisement.objects.create(title='Тест объявление 4', description='тестовое объявление номер 4')
    for _ in range(500000):
        Advertisement.objects.create(title=random.choice(title_list), description=sample_description,
                                     created_at=datetime.datetime.now(), price=random.randint(100, 100000),
                                     views_count=random.randint(0, 200))


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0005_auto_20220110_1618'),
    ]

    operations = [
        migrations.RunPython(gen_advertisement)
    ]
