from django.contrib import admin

from .models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'ip_address', 'status_code', 'time')
    search_fields = ('url',)
    list_filter = ('status_code',)
