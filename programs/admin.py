from .models import Event
from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'name', 'description', 'date', 'start_time', 'location')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Event, EventAdmin)