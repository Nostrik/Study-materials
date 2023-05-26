from django.db import models


class Advertisement(models.Model):
    """Класс - модель объявления"""
    title = models.CharField(max_length=1500, db_index=True, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, default='', verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    author = models.ForeignKey('Author', default=None, verbose_name='Автор объявления', on_delete=models.CASCADE)
    heading = models.ForeignKey('AdvertisementHeading', default=None, verbose_name='Наименование', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisement'
        ordering = ['title']


class Author(models.Model):
    """Класс - модель автора объявления"""
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    email = models.CharField(max_length=50, verbose_name='Эл. почта')
    telephone = models.CharField(max_length=30, verbose_name='Телефон')

    def __str__(self):
        return self.name


class AdvertisementHeading(models.Model):
    """Класс - модель для хранения рубрики объявления"""
    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    birthday = models.DateField()
