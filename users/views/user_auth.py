from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import CreateUserForm, AuthenticationUserForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
  

  action_form = reverse('users:login_user')
  context = {
    'action_form' : action_form,
    'name_button' : 'Autenticar-se',
    'desc_form':'Entre em sua conta e veja as notícias',
    'title_form' : 'Autentique-se'
  }

  if request.method == 'GET':
    form = AuthenticationUserForm(request)
  else:
    form = AuthenticationUserForm(request,request.POST)

    if form.is_valid():
      user = form.get_user()
      login(request,user)
      messages.success(request,'Você está autenticado, parabéns!')
      return redirect('users:dashboard')
    else:
      messages.error(request,'Os dados informados estão incorretos, tente novamente')

  context['form'] = form

  return render(request, 'users/index.html', context)

def create_user(request):

  action_form = reverse('users:create_user')
  context = {
    'action_form' : action_form,
    'name_button' : 'Criar conta',
    'desc_form':'Entre e fique por dentro de todas as notícias da região',
    'title_form' : 'Crie sua conta'
  }

  if request.method == 'GET':
    form = CreateUserForm()
  else:
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Conta criada com sucesso, agora autentique-se!')
      return redirect('users:login_user')


  context['form'] = form 

  return render(request, 'users/index.html', context)

@login_required(login_url='users:login_user')
def logout_user(request):
  logout(request)
  messages.success(request,'Você saiu de sua conta.')
  return redirect('users:login_user')