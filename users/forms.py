from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from users.models import PerfilUser

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


class AlterDataUser(forms.ModelForm):

  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder':'Confirme a senha'}))
  password2 = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class' : 'form-control',
          'placeholder':'Confirme a senha'
        }
      )
    )


  def __init__(self,*args, **kwargs):
    super().__init__(*args,**kwargs)

    self.fields['username'].widget.attrs.update({'class' : 'form-control'})
    self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
    self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
    self.fields['email'].widget.attrs.update({'class' : 'form-control'})

  class Meta:
    fields = ['username','first_name','last_name','email','password1','password2']
    model = User

class PerfilUserForm(forms.ModelForm):

  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.fields['foto_perfil'].widget.attrs.update({'class' : 'form-control'})
    self.fields['descricao'].widget.attrs.update({'class' : 'form-control'})

  def save(self,commit=True,user=User):

    objeto = super().save(commit=False)

    objeto.dono = user

    if commit == True:
      objeto.save()

    return objeto

  class Meta:
    fields = ['foto_perfil','descricao']
    model = PerfilUser
  
  