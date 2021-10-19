from django.contrib import admin

# Register your models here.
from .models import Lugat

class LugatAdmin(admin.ModelAdmin):

    list_display = ['inglizcha', 'uzbekcha']

admin.site.register(Lugat, LugatAdmin)
