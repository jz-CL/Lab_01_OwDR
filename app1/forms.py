from django import forms
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError


User = get_user_model()

class RegisterUserForm(forms.Form):

    # breakpoint()

    name = forms.CharField(label='name')
    surname = forms.CharField(label='surname')
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password')
    password2 = forms.CharField(label='password2')

    # walidacja
    def clean(self):
        # dziedziczymy clean() z Form
        cd = super().clean()

        password = cd['password'] # jest to wymagane pole
        password2 = cd['password2']  # jest to wymagane pole

        if password != password2:
            # zgłaszamy wyjątek
            raise ValidationError('Twoje hasła nie są identyczne!')

        # powinniśmy sprawdzić czy taki użytkownik już jest

        email = cd['email']
        # robimy zapytanie do bazy danych
        # breakpoint()
        if User.objects.filter(email=email).exists():
        #     # exists() zwraca True lub False jeśli istnieje
            raise ValidationError('Ten login jest zajęty')


class LoginUserForm(forms.Form):
    email = forms.EmailField(label='email', required=True)
    password = forms.CharField(label='password', required=True)