from django import forms
from client.models import Client


class StyleFormMixin:
    '''Стилизация'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    '''Формы для CREATE и UPDATE'''

    class Meta:
        model = Client
        fields = ('email', 'name', 'comment', 'owner',)