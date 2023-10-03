from django.contrib import admin
from users.models import PerfilUserBg,PerfilUser,BackgroundDashboard

# Register your models here.
@admin.register(PerfilUserBg)
class ProfileUserBackground(admin.ModelAdmin):
  list_display = ['name_background','utilizar']
  list_editable = ['utilizar']

@admin.register(BackgroundDashboard)
class DashBackground(admin.ModelAdmin):
  list_display = ['name_background','utilizar']
  list_editable = ['utilizar']

@admin.register(PerfilUser)
class ProfileUserAdmin(admin.ModelAdmin):
  ...