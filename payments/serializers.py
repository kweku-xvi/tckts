from .models import TicketPurchase
from rest_framework import serializers


class TicketQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketPurchase
        fields = ['quantity']
