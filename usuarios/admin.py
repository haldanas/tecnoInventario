from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from usuarios.models import Perfil
# Register your models here.

#FORMA1
#admin.site.register(Profile)

#FORMA2
@admin.register(Perfil) 
class PerfilAdmin (admin.ModelAdmin):
    
    list_display = ('pk','usuario','cargo')
    #list_display_linkS = ()
    #list_editable = ()
    search_fields = ('usuario__email','usuario__username','usuario__first_name',
                     'usuario__last_name')
    list_filter = ('u_creado','u_modificado','usuario__is_active','usuario__is_staff')
    
    fieldsets = (
        ('Profile', {
            "fields": (
                ('usuario','cargo'),
            ),
        }),
        ('Metadata', {
            "fields": (
                ('u_creado','u_modificado',),
            ),
        }),
    )
    
    #existen campos que no se pueden editar como las fechas 
    readonly_fields =('u_creado','u_modificado',)
    
# las dos clases espesifican dentro del modulo de user 
# el perfil para qudaar en una sola vista
class PerfilEnLinea(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural ='perfiles'

class UsuarioAdmin(BaseAdmin):
    inline = (PerfilEnLinea,)

admin.site.unregister(User)
admin.site.register(User,UsuarioAdmin)

