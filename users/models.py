from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PerfilUser(models.Model):
  foto_perfil = models.ImageField(upload_to='perfil_picture/%Y/%m/%d')
  descricao = models.TextField()
  dono = models.ForeignKey(User, on_delete=models.CASCADE)

class PerfilUserBg(models.Model):

  class Meta:
    verbose_name = 'Plano de fundo'
    verbose_name_plural = 'Planos de fundo'
  
  name_background = models.CharField(max_length=200)
  background = models.ImageField(upload_to='perfil_bg')
  utilizar = models.BooleanField(default=False)