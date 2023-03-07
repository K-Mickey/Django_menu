from django.contrib import admin
from .models import Menu, MenuCategory


@admin.register(MenuCategory)
class TreeMenuCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'verbose_name', ]
    list_display = ['name', 'verbose_name', ]


@admin.register(Menu)
class TreeMenuAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'path', 'parent', ]
    list_display = ['name', 'path', 'parent', 'category', ]
    list_display_links = ['name', 'path', ]
    search_fields = ['name', ]
    list_filter = ['category', ]
