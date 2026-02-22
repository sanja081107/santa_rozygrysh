from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from main.models import *


# 1. Отключаем стандартное действие удаления
admin.site.disable_action('delete_selected')

# 2. Создаем функцию быстрого удаления
def fast_delete(modeladmin, request, queryset):
    # Метод delete() на queryset удаляет все объекты сразу
    queryset.delete()

# Добавляем описание для админки
fast_delete.short_description = "Удалить выбранные (без подтверждения)"

class CodesResource(resources.ModelResource):
    class Meta:
        model = Codes

class CodesAdmin(ImportExportActionModelAdmin):
    resource_class = CodesResource
    list_display = ('code', 'full_name', 'city')
    list_display_links = ('code', 'full_name')
    search_fields = ('code',)
    ordering = ('id',)
    actions = [fast_delete]

admin.site.register(Codes, CodesAdmin)
