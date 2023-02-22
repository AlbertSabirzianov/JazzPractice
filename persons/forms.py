from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Feetback, PersonalMap


class Registration(UserCreationForm):
    """Форма для отображения регистрации."""
    username = forms.CharField(label='',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'id': "floatingInput",
                                          'placeholder': 'Логин'}
                               )
                               )
    email = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'id': "floatingInput",
                                       'type': 'email',
                                       'placeholder': 'Email'}))
    password1 = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'id': "floatingPassword",
                                                              'type': 'password',
                                                              'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'id': "floatingPassword",
                                                              'type': 'password',
                                                              'placeholder': 'Повторите Пароль'}))
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'id': "floatingInput",
                                                               'placeholder': 'Имя'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'id': "floatingInput",
                                                              'placeholder': 'Фамилия'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    """Форма для отображения логина на сайте."""
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': "floatingInput",
                                                             'placeholder': 'Логин'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'id': "floatingPassword",
                                                                 'type': 'password',
                                                                 'placeholder': 'Пароль'}))


class FeetBackForm(forms.ModelForm):
    """Форма отображения добавления отзыва."""

    class Meta:
        model = Feetback
        fields = ['text', 'stars']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control',
                                                 'id': 'exampleFormControlTextarea1',
                                                 'rows': 5, })
        self.fields['stars'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )


class PersonalMapForm(forms.ModelForm):
    """Форма для редактирования личной информации PersonalMap."""

    class Meta:
        model = PersonalMap
        fields = ['description', 'stady_level', 'stady_course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control',
             'id': 'exampleFormControlTextarea1',
             'rows': 5, }
        )
        self.fields['stady_level'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )
        self.fields['stady_course'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )
