from transactions.forms import TransactionForm
from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email ou Usuário',
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu email ou usuário',
            'required': True
        })
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'required': True
        })
    )