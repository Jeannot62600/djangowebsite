from django.contrib import admin
from project_review.models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name_text_field', 'maj_date')
    
admin.site.register(Type)
admin.site.register(Project, ProjectAdmin)
