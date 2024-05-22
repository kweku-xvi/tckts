from . import views
from django.urls import path


urlpatterns = [
    path('add', views.add_event_view, name='add_event'),
    path('<str:id>/update', views.update_event_view, name='update_event'),
    path('<str:id>/delete', views.delete_event_view, name='delete_event'),
    path('next-week', views.filter_events_in_next_week, name='events_in_next_week'),
    path('next-month', views.filter_events_in_next_month, name='events_in_next_month'),
    path('next-3-months', views.filter_events_in_next_3_months, name='events_in_next_3_months'),
    path('next-6-months', views.filter_events_in_next_6_months, name='events_in_next_6_months'),
    path('search', views.search_events_view, name='search_events'),
    path('<str:id>', views.get_event_info_view, name='event_info'),
]