from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models
from django.utils.translation import gettext as _
from django.db.models import Count
from django.contrib import admin
from .models import Report




admin.site.register(models.Category)







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



admin.site.register(Report)






































