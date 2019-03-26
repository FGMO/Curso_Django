from django.contrib import admin

from usuarios.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'usuario', 'telefono', 'website', 'imagen')
    list_display_links = ('id', 'usuario')
    list_editable = ('website', 'telefono', 'imagen')
    search_fields = ('usuario__id', 'usuario__username', 'usuario__email')
    list_filter = ('usuario__is_active', 'adicionado', 'modificado')