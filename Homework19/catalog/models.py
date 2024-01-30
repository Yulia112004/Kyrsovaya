from django.core.exceptions import ValidationError
from django.db import models

from users.models import User


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    disc = models.CharField(max_length=200, verbose_name='описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_disc = models.CharField(max_length=200, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    data_created = models.DateTimeField(verbose_name='дата создания')
    data_changed = models.DateTimeField(verbose_name='дата последнего изменения')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product_name}'

    def short_des(self):
        return self.product_disc[:100] + '...'

    @property
    def active_version(self):
        return Version.objects.filter(is_active=True, product_id=self.id).first()


    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Contact(models.Model):
    country = models.CharField(max_length=100)
    inn = models.CharField(max_length=12)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.country} ({self.address})"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

class Version(models.Model):
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    version_number = models.IntegerField(verbose_name='номер версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name='продукт')

    def __str__(self):
        return f'{self.version_name} {self.version_number} {self.is_active}'

    def save(self, *args, **kwargs):
        if self.is_active:
            active_versions = Version.objects.filter(product=self.product, is_active=True)
            if self.pk:
                active_versions = active_versions.exclude(pk=self.pk)
            if active_versions.exists():
                raise ValidationError('Может быть только одна активная версия продукта.')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('is_active',)