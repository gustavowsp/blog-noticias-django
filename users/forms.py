from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class CreateUserForm(UserCreationForm):
  
  def __init__(self,*args,**kwargs):
    super().__init__(*args, **kwargs)

    self.fields['username'].widget.attrs.update(
      {
        'placeholder' : 'Apelido',
        'class' : 'form-control'
      }
    )
    self.fields['password1'].help_text = password_validation.password_validators_help_text_html
    self.fields['password1'].widget.attrs.update(
      {
        'placeholder' : 'Senha',
        'class' : 'form-control'
      }
    )
    self.fields['password2'].widget.attrs.update(
      {
        'placeholder' : 'Digite sua senha novamente',
        'class' : 'form-control'
      }
    )

  class Meta:
    fields = ['username','password1','password2']
    model = User

class AuthenticationUserForm(AuthenticationForm):

  def __init__(self, request, *args, **kwargs):
    super().__init__(request, *args, **kwargs)

    self.fields['username'].widget.attrs.update({
      'class' : 'form-control',
      'placeholder' : 'Seu usuário'
    })
    self.fields['password'].widget.attrs.update({
      'class' : 'form-control',
      'placeholder' : 'Sua Senha'
    })