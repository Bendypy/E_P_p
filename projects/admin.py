
from django.contrib import admin
from . import models
from django.utils.translation import gettext as _
from django.db.models import Count
from .models import Report




@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'user', 'category', 'created_at', 'tasks_count']
    list_per_page = 6
    
    list_editable = ['status', 'user', 'category']
    
    
    
    list_select_related = ['category', 'user']
    
    def tasks_count(self, obj):
    #return obj.task_set.count()
        return obj.tasks_count
    def get_queryset(self, request) :
        query = super().get_queryset(request)
        query = query.annotate(tasks_count=Count('task'))
        return query
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_per_page = 6
    list_editable = ['is_completed']



admin.register(models.Report)






































