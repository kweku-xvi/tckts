import uuid
from accounts.models import User
from django.db import models
from programs.models import Event


class TicketType(models.Model):
    ticket_type_id = models.CharField(max_length=5, primary_key=True, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_type')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.name} - {self.event.name}'

    
    def save(self, *args, **kwargs):
        if not self.ticket_type_id:
            self.ticket_type_id = str(uuid.uuid4())[:5]
        super().save(*args, **kwargs)
