from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
# from .models import Item
from .models import Estudiante, Docente, Course, Foro, Direccion, ContactMessage, Inscripcion

class CustomUserAdmin(BaseUserAdmin):
    # Define los campos que deseas mostrar en la lista de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Define los campos que se pueden editar en la página de detalle del usuario
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),  # Ajusta aquí los campos correctos
        ('Permisos', {'fields': ('is_active', 'groups')}),
    )

    # Define los campos que se pueden editar en la página de creación de usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


# class ItemAdmin(admin.ModelAdmin):
#     search_fields = ('name',)
#     list_display_fields =['name','views']
#     list_filter=['views']

# admin.site.register(Item,ItemAdmin)

admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Course)
admin.site.register(Foro)
admin.site.register(Direccion)
admin.site.register(ContactMessage)
admin.site.register(Inscripcion)


class AdminSite(admin.AdminSite):
    site_header = 'Administracion Sitio de Aprendizaje'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio'
    empty_value_display = 'No hay datos para visualizar'

sitio_admin = AdminSite(name='administracion')

sitio_admin.register(Inscripcion)
sitio_admin.register(Estudiante, CustomUserAdmin)
sitio_admin.register(Docente)
sitio_admin.register(Course)

