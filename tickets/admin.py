from .models import TicketType, TicketPurchase
from django.contrib import admin


class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('ticket_type_id', 'name', 'event', 'price')


class TicketPurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_id', 'user', 'event', 'quantity', 'purchased_at')
    readonly_fields = ('purchase_date', 'purchased_at')


admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(TicketPurchase, TicketPurchaseAdmin)