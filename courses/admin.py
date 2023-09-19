from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display_fields =['name','views']
    list_filter=['views']

admin.site.register(Item,ItemAdmin)