from .models import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_id', 'title', 'description', 'image', 'date', 'start_time', 'end_time', 'location', 'address', 'organizer', 'contact_info', 'capacity', 'ticket_price', 'available_tickets', 'status']

        read_only_fields = ['event_id']
