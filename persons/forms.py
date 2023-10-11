from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Feetback, PersonalMap
from Diplom.settings import (
    LOGIN_ATTRS,
    PASSWORD_ATTRS,
    SECOND_PASSWORD_ATTRS,
    TEXT_ATTRS,
    FORM_SELECT
)


class Registration(UserCreationForm):
    """Форма для отображения регистрации."""

    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs=LOGIN_ATTRS
        )
    )
    password1 = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs=PASSWORD_ATTRS
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs=SECOND_PASSWORD_ATTRS
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    """Форма для отображения логина на сайте."""

    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs=LOGIN_ATTRS
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs=PASSWORD_ATTRS
        )
    )


class FeetBackForm(forms.ModelForm):
    """Форма отображения добавления отзыва."""

    class Meta:
        model = Feetback
        fields = ['text', 'stars']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(TEXT_ATTRS)
        self.fields['stars'].widget.attrs.update(FORM_SELECT)


class PersonalMapForm(forms.ModelForm):
    """Форма для редактирования личной информации PersonalMap."""

    class Meta:
        model = PersonalMap
        fields = ['description', 'stady_level', 'stady_course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update(TEXT_ATTRS)
        self.fields['stady_level'].widget.attrs.update(FORM_SELECT)
        self.fields['stady_course'].widget.attrs.update(FORM_SELECT)
