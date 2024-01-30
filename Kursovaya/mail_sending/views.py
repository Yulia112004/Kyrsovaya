from django.shortcuts import render
from random import sample
from mail_sending.models import Message, Mailing, Log
from client.models import Client
from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from mail_sending.forms import MailingForm, MessageForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from mail_sending.mailing_services import send_mailing


'''ГЛАВНАЯ'''
# --------------------------------------------------------------------------------------------------------------------------------

def index(request):
    '''Главная страница'''
    total_mailings = Mailing.objects.count()  # всего рассылок
    # active_mailings = Mailing.objects.filter(status='running').count()  # всего активных рассылок
    unique_clients = Client.objects.distinct().count()  # всего уникальных клиентов
    all_posts = Blog.objects.filter(is_published=True)  # все блог-посты

    if len(all_posts) >= 3:
        random_posts = sample(list(all_posts), 3)  # 3 случайных блог-поста
    elif len(all_posts) == 0:
        random_posts = None
    else:
        random_posts = sample(list(all_posts), 1)

    context = {'total_mailings': total_mailings,
               # 'active_mailings': active_mailings,
               'unique_clients': unique_clients,
               'posts': random_posts}

    return render(request, 'mail_sending/index.html', context)



'''РАССЫЛКИ - Mailing'''
# --------------------------------------------------------------------------------------------------------------------------------

class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    '''CREATE - создается карточка рассылки'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail_sending:mail_sending_index')
    permission_required = 'mail_sending.add_mailing'

    #def form_valid(self, form):
        #if form.is_valid():
            #new_mat = form.save()
            #new_mat.save()

        #return super().form_valid(form)

    def form_valid(self, form):
        self.object = form.save()
        self.object.status_mail = 'created'
        self.object.save()
        if self.object.status_mail in ('running', 'created'):
            send_mailing(self.object)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)



class MailingListView(LoginRequiredMixin, ListView):
    '''READ - чтение списка рассылок'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''

    model = Mailing
    template_name = 'mail_sending/mail_sending_index.html'


class MailingDetailView(LoginRequiredMixin, DetailView):
    '''READ - чтение одной рассылки'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''

    model = Mailing
    success_url = reverse_lazy('mail_sending:mail_sending_detail')


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    '''UPDATE - обновление записи рассылки'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail_sending:mail_sending_index')
    permission_required = 'mail_sending.change_mailing'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mail_sending:mail_sending_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''DELETE - удаление записи рассылки'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Mailing
    success_url = reverse_lazy('mail_sending:mail_sending_index')
    permission_required = 'mail_sending.delete_mailing'



'''СООБЩЕНИЕ - Message'''
# --------------------------------------------------------------------------------------------------------------------------------

class MessageCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    '''CREATE - создается сообщение'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_sending:message_index')
    permission_required = 'mail_sending.add_message'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    '''READ - чтение списка сообщений'''

    model = Message
    template_name = 'mail_sending/message_index.html'


class MessageDetailView(LoginRequiredMixin, DetailView):
    '''READ - чтение одного сообщения'''

    model = Message
    success_url = reverse_lazy('mail_sending:message_detail')


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    '''UPDATE - обновление сообщения'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_sending:message_index')
    permission_required = 'mail_sending.change_message'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mail_sending:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''DELETE - удаление сообщения'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Message
    success_url = reverse_lazy('mail_sending:message_index')
    permission_required = 'mail_sending.delete_message'


'''ЛОГИ - log'''
# --------------------------------------------------------------------------------------------------------------------------------

class LogListView(LoginRequiredMixin, ListView):
    '''READ - чтение списка логов'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''

    model = Log
    template_name = 'mail_sending/log_index.html'


class LogDetailView(LoginRequiredMixin, DetailView):
    '''READ - чтение одного лога'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''

    model = Log
    success_url = reverse_lazy('mail_sending:log_detail')