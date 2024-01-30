from django.urls import path
from mail_sending.views import index
from mail_sending.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView
from mail_sending.views import MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView
from mail_sending.views import LogListView, LogDetailView

from .apps import MailSendingConfig

app_name = MailSendingConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('mail_sending/', MailingListView.as_view(), name='mail_sending_index'),
    path('mail_sending/create/', MailingCreateView.as_view(), name='mail_sending_create'),
    path('mail_sending_detail/<int:pk>/', MailingDetailView.as_view(), name='mail_sending_detail'),
    path('mail_sending/update/<int:pk>/', MailingUpdateView.as_view(), name='mail_sending_update'),
    path('mail_sending/delete/<int:pk>/', MailingDeleteView.as_view(), name='mail_sending_delete'),
    path('message/', MessageListView.as_view(), name='message_index'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('log/', LogListView.as_view(), name='log_index'),
    path('log_detail/<int:pk>/', LogDetailView.as_view(), name='log_detail'),

]