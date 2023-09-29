from django.contrib import admin
from .models import Log
from django.utils.safestring import mark_safe

class LogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip', 'user_agent', 'accept_language', 'get_image_url')
    list_filter  = ('timestamp',)

    def get_image_url(self, obj):
        return mark_safe(f'<img src="/" class="img-fluid-flag" alt="{obj.accept_language}" id={obj.id}>')
    
    get_image_url.short_description = 'Preview'

    class Media:
        js = ['logs/js/flag.js']

admin.site.register(Log, LogAdmin)
