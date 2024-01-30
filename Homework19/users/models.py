from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}



class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    country = models.CharField(max_length=50, verbose_name='Страна')
    avatar = models.ImageField(upload_to='users/', verbose_name='Фото')
    verified = models.BooleanField(default=False, verbose_name='верифицирован', blank=True)
    verified_password = models.IntegerField(verbose_name='ключ для верификации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []