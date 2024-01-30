from django import forms
from blog.models import Blog


class StyleFormMixin:
    '''Стилизация'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, forms.ModelForm):
    '''Формы для CREATE и UPDATE'''

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'data_create', 'is_published', 'views_count',)