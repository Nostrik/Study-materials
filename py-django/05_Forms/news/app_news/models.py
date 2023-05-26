from django.db import models


class News(models.Model):

    STATUS_CHOICES = [
        (True, 'Активно'),
        (False, 'Неактивно'),
    ]
    title = models.CharField(max_length=1500, db_index=True, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, default='', verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    actual = models.BooleanField(verbose_name='Актуальность', choices=STATUS_CHOICES, default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):

    ADMIN_CHOICES = [
        ('d', 'Удалено администратором')
    ]
    user_name = models.CharField(max_length=1500, db_index=True, verbose_name='Имя пользователя')
    text = models.TextField(max_length=1000, default='', verbose_name='Текст комментария')
    news = models.ForeignKey('News', verbose_name='Новость', related_name='comments', on_delete=models.CASCADE)
    administration = models.CharField(max_length=30, verbose_name='Администрирование', choices=ADMIN_CHOICES, default='')

    def __str__(self):
        return self.user_name
