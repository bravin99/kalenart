from django.contrib import admin
from main_app.models import SiteData


@admin.register(SiteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = ['header_title', 'created', 'updated']

