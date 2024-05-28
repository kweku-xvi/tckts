from .models import TicketType, TicketPurchase
from rest_framework import serializers


class TicketTypeSerializer(serializers.ModelSerializer):
    event = serializers.SerializerMethodField()


    class Meta:
        model = TicketType
        fields = ['ticket_type_id', 'name', 'event', 'price', 'quantity_available']

        read_only_fields = ['ticket_type_id']

    
    def get_event(self, obj):
        return obj.event.name if obj.event else None



class TicketPurchaseSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()
    ticket_type = serializers.SerializerMethodField()


    class Meta:
        model = TicketPurchase
        fields = ['purchase_id', 'user', 'event', 'ticket_type', 'quantity']

        read_only_fields = ['purchase_id']

    
    def get_user(self, obj):
        return obj.user.username if obj.user else None

    
    def get_event(self, obj):
        return obj.event.name if obj.event else None


    def get_ticket_type(self, obj):
        return obj.ticket_type.name if obj.ticket_type else None