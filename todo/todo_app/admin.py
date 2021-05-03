from django.contrib import admin

from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'in_date', 'out_date')
    search_fields = ('title', 'text')


admin.site.register(task, TaskAdmin)


class FileAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'path')


admin.site.register(file, FileAdmin)
