from django.contrib import admin

from usuarios.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('usuario', 'telefono', 'website', 'imagen')
