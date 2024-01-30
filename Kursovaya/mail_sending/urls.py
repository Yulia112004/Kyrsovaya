from django.urls import path
from mail_sending.views import index
from mail_sending.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView

from .apps import MailSendingConfig

app_name = MailSendingConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('mail_sending/', MailingListView.as_view(), name='mail_sending_index'),
    path('mail_sending/create/', MailingCreateView.as_view(), name='mail_sending_create'),
    path('mail_sending_detail/<int:pk>/', MailingDetailView.as_view(), name='mail_sending_detail'),
    path('mail_sending/update/<int:pk>/', MailingUpdateView.as_view(), name='mail_sending_update'),
    path('mail_sending/delete/<int:pk>/', MailingDeleteView.as_view(), name='mail_sending_delete'),
]