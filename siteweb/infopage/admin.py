from django.contrib import admin
from infopage.models import *

class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'maj_date')

admin.site.register(Info, InfoAdmin)
