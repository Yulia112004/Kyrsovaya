from django.utils import timezone
from django.db import models

# Create your models here.
# Constants
NULLABLE = {'blank': True, 'null': True}


# Blog.
class Blog(models.Model):
    '''Блог сервиса'''
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(**NULLABLE, upload_to='blog/', verbose_name='Изображение')
    data_create = models.DateField(**NULLABLE, default=timezone.now, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('title',)