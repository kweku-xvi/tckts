import uuid
from accounts.models import User
from django.db import models
from PIL import Image


class Event(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ]


    event_id = models.CharField(unique=True, primary_key=True, max_length=13)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    address = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.PositiveIntegerField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    available_tickets = models.PositiveIntegerField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Upcoming')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'

    
    def save(self, *args, **kwargs):
        if not self.event_id:
            self.event_id = str(uuid.uuid4())[:13]
        super().save(*args, **kwargs)

    
    class Meta:
        ordering = ('-created_at',)