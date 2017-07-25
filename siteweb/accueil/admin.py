from django.contrib import admin
from accueil.models import *

class PartAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Part, PartAdmin)
