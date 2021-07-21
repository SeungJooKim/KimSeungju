from django.contrib import admin
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name','kind']
    list_display_links =['name']
    search_fields=['name']
    pass
