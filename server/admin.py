from django.contrib import admin
from .models import Menu, MenuCategory


@admin.register(MenuCategory)
class TreeMenuCategoryAdmin(admin.ModelAdmin):

    fields = ['name', 'verbose_name', ]
    list_display = ['__str__', ]


@admin.register(Menu)
class TreeMenuAdmin(admin.ModelAdmin):

    fields = ['name', 'category', 'path', 'parent', ]
    list_display = ['__str__', 'category', 'path', 'parent', ]
