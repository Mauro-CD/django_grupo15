from django.contrib import admin

# Register your models here.
# from .models import Item
from .models import Estudiante, Docente, Course, Foro, Direccion, ContactMessage, Inscripcion

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

# @admin.register(Estudiante)
# class EstudianteAdmin(admin.ModelAdmin):
#     list_display = ('nombre')