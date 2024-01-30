from mail_sending.models import Mailing
from mail_sending.mailing_services import send_mailing


def daily_send():
    '''Ежедневная рассылка'''
    for item in Mailing.objects.filter(period_mail='daily'):
        item.status_mail = 'running'
        item.save()
        send_mailing(item)
        item.status_mail = 'completed'
        item.save()


def weekly_send():
    '''Еженедельная рассылка'''
    for item in Mailing.objects.filter(period_mail='weekly'):
        item.status_mail = 'running'
        item.save()
        send_mailing(item)
        item.status = 'completed'
        item.save()


def monthly_send():
    '''Ежемесячная рассылка'''
    for item in Mailing.objects.filter(period_mail='monthly'):
        item.status_mail = 'running'
        item.save()
        send_mailing(item)
        item.status_mail = 'completed'
        item.save()