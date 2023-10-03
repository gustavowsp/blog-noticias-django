from django.shortcuts import render
from django.urls import reverse
from users.models import PerfilUserBg, PerfilUser,BackgroundDashboard
from users.forms import PerfilUserForm, AlterDataUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def pegar_foto_perfil(user):

  perfil = PerfilUser.objects.get(dono=user)
  return perfil

@login_required(login_url=('users:login_user'))
def create_perfiluser(request):

  background = PerfilUserBg.objects.filter(utilizar=True)[0]
  # Criando os formulários vazios
  form = AlterDataUser(instance=request.user)
  
  # Checando se o usuário já possui um perfil
  try:
    perfil_user = PerfilUser.objects.get(dono=request.user)
  except:
    perfil_user = None

  if request.method == 'GET':

    # Se tiver perfil vamos retornar o perfil ao usuário visualizar
    if perfil_user:
      perfil_form = PerfilUserForm(instance = perfil_user)
    else:
      perfil_form = PerfilUserForm()

  else:
    # Caso o usuário tenha perfil vamos atualiza-lo.
    if perfil_user:
      perfil_form = PerfilUserForm(request.POST,request.FILES, instance=perfil_user)
    else:
      perfil_form = PerfilUserForm(request.POST,request.FILES)
    
    if perfil_form.is_valid():
      perfil_form.save(user=request.user)
      messages.success(request, 'Dados Do Perfil Atualizados')

  # Criando actions_forms
  action_perfil_user = reverse('users:create_perfil_user') 
  action_form = reverse('users:alter_data_user')

  context = {
    'image_url' : background,
    'form' : form,
    
    # Para o perfil de usuário
    'perfil_form' : perfil_form,
    'action_form_perfil' : action_perfil_user,
    'name_button_perfil_user' : 'Atualizar Perfil',

    # Para os dados do usuário
    'action_form' : action_form,
    'name_button' : 'Atualizar conta',
  }
  if perfil_user:
    context['profile_photo'] = perfil_user

  return render(request,'users/change_perfil_user.html', context)

@login_required(login_url=('users:login_user'))
def update_data_user(request):
  
  background = PerfilUserBg.objects.filter(utilizar=True)[0]
  
  # Checando se o usuário já possui um perfil
  try:
    perfil_user = PerfilUser.objects.get(dono=request.user)
  except:
    perfil_user = None

  # Se tiver perfil vamos retornar o perfil ao usuário visualizar
  if perfil_user:
    perfil_form = PerfilUserForm(instance=perfil_user)
  else:
    perfil_form = PerfilUserForm()


  # Criando os formulários vazios
  if request.method == 'GET':
    form = AlterDataUser(instance=request.user)

  else:
    form = AlterDataUser(request.POST, instance=request.user)

    if form.is_valid():
      form.save()
      messages.info(request,'Dados atualizados')


  # Criando actions_forms
  action_perfil_user = reverse('users:create_perfil_user') 
  action_form = reverse('users:alter_data_user')

  context = {
    'image_url' : background,
    'form' : form,
    
    # Para o perfil de usuário
    'perfil_form' : perfil_form,
    'action_form_perfil' : action_perfil_user,
    'name_button_perfil_user' : 'Atualizar Perfil',

    # Para os dados do usuário
    'action_form' : action_form,
    'name_button' : 'Atualizar conta',
  }
  if perfil_user:
    context['profile_photo'] = perfil_user

  return render(request,'users/change_perfil_user.html', context)

@login_required(login_url=('users:login_user'))
def dashboard_user(request):

  try:
    background = BackgroundDashboard.objects.get(utilizar=True)
  except:
    background = None

  if PerfilUser.objects.filter(dono=request.user).exists():
    profile_photo = PerfilUser.objects.get(dono=request.user)


  context = {
    'image_url' : background,
    'profile_photo' : profile_photo,
    'perfil_user' : profile_photo,
  }

  return render(request,'users/dashboard.html', context)