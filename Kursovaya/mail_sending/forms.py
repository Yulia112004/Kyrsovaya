from django import forms
from mail_sending.models import Mailing, Message, Log


class StyleFormMixin:
    '''Стилизация'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    '''Формы рассылки для CREATE и UPDATE'''

    class Meta:
        model = Mailing
        fields = ('title', 'client', 'time_mail', 'period_mail', 'status_mail',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    '''Сообщение'''

    class Meta:
        model = Message
        fields = '__all__'


class LogForm(StyleFormMixin, forms.ModelForm):
    '''Логи'''

    class Meta:
        model = Log
        fields = '__all__'