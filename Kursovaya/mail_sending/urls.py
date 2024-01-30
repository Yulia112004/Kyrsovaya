from django.urls import path
from mail_sending.views import index
from .apps import MailSendingConfig

app_name = MailSendingConfig.name

urlpatterns = [
    path('', index)
]