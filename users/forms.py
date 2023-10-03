from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from users.models import PerfilUser
from django.core.exceptions import ValidationError

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

  password1 = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class' : 'form-control', 'placeholder':'Digite sua nova senha'
        }
      ),
      label='Senha',
      required=False,
      help_text= password_validation.password_validators_help_text_html
    )
  password2 = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class' : 'form-control',
          'placeholder':'Confirme a senha'
        }
      ),
      label='Confirmação da senha',
      required=False
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

  def save(self,commit=True):

    usuario = super().save(commit=False)

    password = self.cleaned_data.get('password1')
    
    if password:
      usuario.set_password(password)

    if commit:
      usuario.save()

    return usuario
    

  def clean(self):

    data = self.cleaned_data
    senha = data.get('password1')
    confirmacao_senha = data.get('password2')

    if senha or confirmacao_senha:
      if senha != confirmacao_senha:
        self.add_error('password2', ValidationError('As senhas não coincidem...'))

    return super().clean()

  def clean_email(self):

    email = self.cleaned_data.get('email').lower()
    print(email)
    
    # Checando se email já existe no banco de dados
    consulta_email = User.objects.filter(email=email)

    if consulta_email.exists():

      email_atual_usuario = consulta_email[0].email.lower()

      if email_atual_usuario != self.instance.email:
        self.add_error(
          'email',
          ValidationError('Este email já está sendo utilizado...',code='invalid')
          )

    return email

  def clean_password1(self):

    password1 = self.cleaned_data.get('password1')

    if password1:
      try:
        password_validation.validate_password(password1)
      except ValidationError as errors:
        self.add_error('password1', ValidationError(errors,code='invalid'))

    return password1

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
  
  