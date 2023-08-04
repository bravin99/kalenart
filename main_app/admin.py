from django.contrib import admin
from main_app.models import SiteData, Feed


@admin.register(SiteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = ['header_title', 'created', 'updated']


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ["description", ]
    list_filter = ["display", "created", "updated"]
