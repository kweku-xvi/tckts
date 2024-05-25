from .models import TicketType
from rest_framework import serializers


class TicketTypeSerializer(serializers.ModelSerializer):
    event = serializers.SerializerMethodField()


    class Meta:
        model = TicketType
        fields = ['ticket_type_id', 'name', 'event', 'price', 'quantity_available']

        read_only_fields = ['ticket_type_id']

    
    def get_event(self, obj):
        return obj.event.name if obj.event else None