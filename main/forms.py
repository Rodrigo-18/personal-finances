
from django.http import request
from main.models import Balanco, Despesa, Receita
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

class DespesaForm(forms.ModelForm):
   class Meta:
      model = Despesa
      fields = [
        'descricao',
        'valor',
        'date',
      ]
      labels = {
          'date': ('Descricao'),
      }
      widgets = {
            'date': forms.DateInput(attrs={
                        'type':'date',
                }), 
        }


class ReceitaForm(forms.ModelForm):
   class Meta:
      model = Receita
      fields = [
        'descricao',
        'valor',
        'date',
      ]
      labels = {
          'date': ('Descricao'),
      }
      widgets = {
            'date': forms.DateInput(attrs={
                        'type':'date',
                }), 
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={
                        'placeholder':'Username',
                }), 
        }
        error_messages = {
            'username': {
                'unique': 'Digite outro nome de usuário',
            },
            'password_mismatch':'Senhas não coincidem'}
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Sua senha'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
