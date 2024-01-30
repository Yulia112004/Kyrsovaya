from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from blog.forms import BlogForm
from blog.models import Blog
from pytils.translit import slugify

from django.core.mail import send_mail
from django.conf import settings


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'date')
    success_url = reverse_lazy('blog:list')
    extra_context = {
        'title': 'Новый блог:'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            send_mail(subject="Django Blog",
                      message=f'Поздравляю! У Вас 100 просмотров по записи "{self.object.title}" в блоге!',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=['byckovaulia669@gmail.com'],
                      fail_silently=False
                      )
            self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'date')
    extra_context = {
        'title': 'Редактировать блог:'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('slug')])
