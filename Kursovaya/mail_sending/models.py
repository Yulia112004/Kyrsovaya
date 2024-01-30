from django.utils import timezone
from django.db import models
from client.models import Client
from users.models import User

# Create your models here.
# Constants

NULLABLE = {'blank': True, 'null': True}

PERIOD_MAIL = (
    ('daily', 'Раз в день'),
    ('weekly', 'Раз в неделю'),
    ('monthly', 'Раз в месяц'),
)

STATUS_MAIL = (
    ('created', 'Создана'),
    ('running', 'Запущена'),
    ('completed', 'Завершена'),
)

STATUS_LOG = (
    ('success', 'Успешно'),
    ('failure', 'Ошибка'),
)


# Message
class Message(models.Model):
    '''Сообщение для рассылки'''
    title = models.CharField(max_length=100, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Тело письма')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
        ordering = ('title',)


# Mailing

class Mailing(models.Model):
    '''Рассылка'''
    title = models.CharField(max_length=100, verbose_name='Название')
    client = models.ManyToManyField(Client, verbose_name='Клиенты для рассылки')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Сообщение')
    time_mail = models.DateTimeField(default=timezone.now, verbose_name='Время рассылки')
    period_mail = models.CharField(max_length=50, verbose_name='Период рассылки', choices=PERIOD_MAIL)
    status_mail = models.CharField(max_length=50, default='created', verbose_name='Статус рассылки',
                                   choices=STATUS_MAIL)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('time_mail',)


class Log(models.Model):
    '''Логи рассылки'''
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, **NULLABLE, verbose_name='Рассылка')
    datetime_attempt = models.DateTimeField(default=timezone.now, verbose_name='Дата последней попытки')
    status_attempt = models.CharField(choices=STATUS_LOG, max_length=50, verbose_name='Статус попытки')
    answer_server = models.TextField(**NULLABLE, verbose_name='Ответ сервера')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, **NULLABLE, verbose_name='Сообщение')

    def __str__(self):
        return f"Время рассылки: {self.datetime_attempt}"

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('datetime_attempt',)