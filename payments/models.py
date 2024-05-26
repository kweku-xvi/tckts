from .utils import generate_payment_id
from accounts.models import User
from django.db import models
from programs.models import Event
from tickets.models import TicketType


class TicketPurchase(models.Model):
    ticket_id = models.CharField(max_length=10, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name='tickets')
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    purchase_date = models.DateTimeField()
    purchased_at = models.DateTimeField()


    def __str__(self):
        return f'{self.ticket_code} - {self.ticket_type.name}'


    def save(self, *args, **kwargs):
        if not self.ticket_id:
            self.ticket_id = generate_payment_id(10)
        super().save(*args, **kwargs)

    
    class Meta:
        ordering = ('-purchased_at',)