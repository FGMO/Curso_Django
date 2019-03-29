from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from usuarios.models import Perfil

# Register your models here.


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    list_display = ('id', 'usuario', 'telefono', 'website', 'imagen')
    list_display_links = ('id', 'usuario')
    list_editable = ('website', 'telefono', 'imagen')
    search_fields = ('usuario__id', 'usuario__username', 'usuario__email')
    list_filter = ('usuario__is_active', 'adicionado', 'modificado')

    fieldsets = (
        ('Perfil', {
            'fields': (('usuario', 'imagen'),)
        }),
        ('Extra info', {
            'fields': (
                ('telefono', 'website'),
                ('biografia')
            )
        }),
        ('Metadata', {
            'fields':(('adicionado', 'modificado'),)
        })
    )

    readonly_fields = ('adicionado', 'modificado')

class ProfileInLine(admin.StackedInline):

    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfiles'

class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInLine, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)