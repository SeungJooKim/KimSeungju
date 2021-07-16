from django.contrib import admin
from .models import Item

# 등록법 1
# admin.site.register(Item)

# 등록법 2
# class ItemAdmin(admin.ModelAdmin):
#    pass

# 등록법 3


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'short_desc', 'is_publish']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['is_publish']

    def short_desc(self, item):
        return item.desc[:10]
