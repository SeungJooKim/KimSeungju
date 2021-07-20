from django.contrib import admin

from .models import Idea

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title','desc']
    list_display_links =['title']
    search_fields=['title']
    pass
