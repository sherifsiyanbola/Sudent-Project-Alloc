from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Project

# class ProjectAdmin(admin.ModelAdmin):
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('id','manager', 'regno', 'name', 'projecttitle', 'department', 'projecttype', 'first_choice_supervisor', 'second_choice_supervisor', 'third_choice_supervisor')
    list_per_page = 5
    search_fields = ('name', 'regno', 'manager', 'department', 'first_choice_supervisor', 'second_choice_supervisor', 'third_choice_supervisor', 'projecttype')
    list_filter = ('name', 'regno', 'manager', 'department', 'first_choice_supervisor', 'second_choice_supervisor', 'third_choice_supervisor', 'projecttype')
    
admin.site.register(Project, ProjectAdmin)
# admin.site.unregister(Group)
