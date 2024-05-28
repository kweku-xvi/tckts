from .utils import generate_id
from accounts.models import User
from django.db import models
from tickets.models import TicketPurchase


class Payment(models.Model):
    payment_id = models.CharField(max_length=20, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase = models.OneToOneField(TicketPurchase, on_delete=models.CASCADE, blank=True, null=True)
    paid_at = models.DateTimeField()


    def __str__(self):
        return f'{self.payment_id} - {self.user.username} - {self.amount}'

    
    class Meta:
        ordering = ('-paid_at',)