from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
  
  #Auth User
  path('create/', views.create_user, name='create_user'),
  path('login/', views.login_user, name='login_user'),
  path('logout/', views.logout_user, name='logout_user'),

  #Perfil User
  path('data-perfil/', views.create_perfiluser, name='create_perfil_user'),
]