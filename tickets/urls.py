from . import views
from django.urls import path

urlpatterns = [
    path('<str:event_id>/add', views.add_ticket_type_view, name='add_ticket_type'),
    path('<str:ticket_type_id>/update', views.update_ticket_type_info_view, name='update_ticket_type'),
    path('<str:ticket_type_id>/delete', views.delete_ticket_type_view, name='delete_ticket_type'),
    path('<str:event_id>', views.get_event_ticket_types_view, name='event_ticket_types_view'),
]