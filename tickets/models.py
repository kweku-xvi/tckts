import uuid
from accounts.models import User
from django.db import models
from payments.utils import generate_payment_id
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


class TicketPurchase(models.Model):
    purchase_id = models.CharField(max_length=10, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name='tickets')
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateField(auto_now_add=True)
    purchased_at = models.DateTimeField(auto_now_add=True)
    payment_verified = models.BooleanField(default=False)


    def total_amount(self):
        return self.ticket_type.price * self.quantity


    def __str__(self):
        return f'{self.purchase_id} - {self.ticket_type.name}'

    
    def save(self, *args, **kwargs):
        if not self.purchase_id:
            self.purchase_id = generate_payment_id(10)
        super().save(*args, **kwargs)

    
    class Meta:
        ordering = ('-purchased_at',)