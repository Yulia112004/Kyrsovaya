from django.shortcuts import render
from random import sample
from mail_sending.models import Message, Mailing, Log
from client.models import Client
from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from mail_sending.forms import MailingForm

# Create your views here.
def index(request):
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


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail_sending:mail_sending_index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing
    template_name = 'mail_sending/mail_sending_index.html'


class MailingDetailView(DetailView):
    model = Mailing
    success_url = reverse_lazy('mail_sending:mail_sending_detail')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail_sending:mail_sending_index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mail_sending:mail_sending_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mail_sending:mail_sending_index')