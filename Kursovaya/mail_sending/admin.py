from django.contrib import admin

# Register your models here.
from mail_sending.models import Mailing, Message, Log


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text',)
    search_fields = ('title',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_mail', 'period_mail', 'status_mail',)
    search_fields = ('title', 'period_mail', 'status_mail',)
    list_filter = ('time_mail', 'period_mail', 'status_mail',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('datetime_attempt', 'status_attempt', 'answer_server',)
    search_fields = ('datetime_attempt', 'status_attempt', 'answer_server',)
    list_filter = ('datetime_attempt', 'status_attempt', 'answer_server',)