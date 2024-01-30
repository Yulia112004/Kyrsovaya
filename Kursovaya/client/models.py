from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    '''Клиент сервиса'''
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(**NULLABLE, max_length=150, verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.email} {self.name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'