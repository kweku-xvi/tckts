from . import views
from django.urls import path


urlpatterns = [
    path('<str:ticket_type_id>', views.buy_tickets, name='checkout'),
    path('webhook', views.payment_webhook, name='payment_webhook')
]