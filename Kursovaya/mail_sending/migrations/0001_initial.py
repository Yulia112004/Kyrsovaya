# Generated by Django 5.0.1 on 2024-01-30 16:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема письма')),
                ('text', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'письмо',
                'verbose_name_plural': 'письма',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('time_mail', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время рассылки')),
                ('period_mail', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=50, verbose_name='Период рассылки')),
                ('status_mail', models.CharField(choices=[('created', 'Создана'), ('running', 'Запущена'), ('completed', 'Завершена')], default='created', max_length=50, verbose_name='Статус рассылки')),
                ('client', models.ManyToManyField(to='client.client', verbose_name='Клиенты для рассылки')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mail_sending.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
                'ordering': ('time_mail',),
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_attempt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата последней попытки')),
                ('status_attempt', models.CharField(choices=[('success', 'Успешно'), ('failure', 'Ошибка')], max_length=50, verbose_name='Статус попытки')),
                ('answer_server', models.TextField(blank=True, null=True, verbose_name='Ответ сервера')),
                ('mailing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mail_sending.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
                'ordering': ('datetime_attempt',),
            },
        ),
    ]
