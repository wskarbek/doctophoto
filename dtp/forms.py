from dtp.models import Examination
from django import forms
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'username': 'Nazwa użytownika',
            'email': 'Adres e-mail',
            'password': 'Hasło'
        }
        widgets = {
            'password': PasswordInput(attrs={'class': 'form-control'})
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Nazwa użytkownika',
            'password': 'Hasło'
        }
        widgets = {
            'password': PasswordInput(attrs={'class': 'form-control'})
        }


class AddExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ['title', 'description', 'patient']
        labels = {
            'title' : 'Tytuł',
            'description' : 'Deskrypcja',
            'patient': 'Pacjent'
        }
        widgets = {
        }