from django.contrib import admin
from todo.models import Task, Category

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'completed',
        'created_at',
        'date_end',
        'category'
    )

admin.site.register(Task, TaskAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

admin.site.register(Category, CategoryAdmin)
# Register your models here.
