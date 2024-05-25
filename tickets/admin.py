from .models import TicketType
from django.contrib import admin


class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('ticket_type_id', 'name', 'event')


admin.site.register(TicketType, TicketTypeAdmin)