from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    # author = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100, default='', verbose_name='Заголовок')
    text = models.TextField(max_length=3000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # file = models.FileField(blank=True)

    def __str__(self):
        return self.title


class Picture(models.Model):
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class UploadFileUpd(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
