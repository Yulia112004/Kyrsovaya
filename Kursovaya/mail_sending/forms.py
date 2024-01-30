from django import forms
from mail_sending.models import Mailing


class StyleFormMixin:
    '''Стилизация'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    '''Формы для CREATE и UPDATE'''

    class Meta:
        model = Mailing
        fields = ('title', 'client', 'message', 'time_mail', 'period_mail', 'status_mail',)