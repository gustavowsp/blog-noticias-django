from django.shortcuts import render
from django.urls import reverse
from users.models import PerfilUserBg, PerfilUser
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
  form = AlterDataUser()
  
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
      perfil_form = PerfilUserForm(request.POST,request.FILES, instance=perfil_user)
    
    if perfil_form.is_valid():
      perfil_form.save(user=request.user)
      messages.success(request, 'Dados Do Perfil Atualizados')

  # Criando actions_forms
  action_perfil_user = reverse('users:create_perfil_user') 
  action_form = reverse

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