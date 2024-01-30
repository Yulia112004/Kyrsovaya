from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class StyleFormMixin:
    '''Стилизация'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    '''Регистрация пользователя'''

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    '''Профиль пользователя'''

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'surname', 'email', 'password', 'avatar', 'phone', 'country', 'comment', 'is_verified')

    def __init__(self, *args, **kwargs):
        '''Скрыть пароль в профиле'''
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()