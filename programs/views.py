from .models import Event
from .serializers import EventSerializer
from accounts.models import User
from accounts.permissions import IsVerified
from datetime import timedelta
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


def get_event(id:str):
    try:
        event = Event.objects.get(event_id=id)
    except Event.DoesNotExist:
        return Response(
            {
                'success':False,
                'message':'Event not found'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return event


def get_events_timeframe(days:int):
    now = timezone.now()
    timeframe = now + timedelta(days=days)
    events = Event.objects.filter(date__gte=now.date(), date__lte=timeframe.date())
    return events


@api_view(['POST'])
@permission_classes([IsVerified])
def add_event_view(request):
    if request.method == 'POST':
        organizer = request.user 
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(organizer=organizer)

            return Response(
                {
                    'success':True,
                    'message':'Event created successfully',
                    'event':serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'success':True,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['PUT', 'PATCH'])
@permission_classes([IsVerified])
def update_event_view(request, id:str):
    if request.method == 'PUT' or request.method == 'PATCH':
        current_user = request.user
        event = get_event(id=id)

        if current_user != event.organizer and not current_user.is_staff:
            return Response(
                {
                    'success':False,
                    'message':"You don't have the permission to make changes to this event"
                }, status=status.HTTP_403_FORBIDDEN
            )

        serializer = EventSerializer(event, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'success':True,
                    'message':'Event updated successfully',
                    'event':serializer.data
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                'success':True,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )
        

@api_view(['GET'])
def get_event_info_view(request, id:str):
    if request.method == 'GET':
        event = get_event(id=id)
        serializer = EventSerializer(event)

        return Response(
            {
                'success':True,
                'event':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_event_view(request, id:str):
    if request.method == 'DELETE':
        current_user = request.user
        event = get_event(id=id)

        if current_user != event.organizer and not current_user.is_staff:
            return Response(
                {
                    'success':False,
                    'message':"You don't have the permission to delete this event"
                }, status=status.HTTP_403_FORBIDDEN
            )

        event.delete()

        return Response(
            {
                'success':True,
                'message':'Event successfully deleted'
            }, status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET'])
def search_events_view(request):
    if request.method == 'GET':
        title = request.query_params.get('title')

        if not title:
            return Response(
                {
                    'success':False,
                    'message':'Title is required'
                }, status=status.HTTP_400_BAD_REQUEST
            )

        events = Event.objects.filter(title__icontains=title)
        serializer = EventSerializer(events, many=True)

        return Response(
            {
                'success':True,
                'message':'Search results:',
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
def filter_events_in_next_week(request):
    if request.method == 'GET':
        events = get_events_timeframe(days=7)

        serializer = EventSerializer(events, many=True)

        return Response(
            {
                'success':True,
                'message':'Upcoming events in the next week:',
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )

        
@api_view(['GET'])
def filter_events_in_next_month(request):
    if request.method == 'GET':
        events = get_events_timeframe(days=30)

        serializer = EventSerializer(events, many=True)

        return Response(
            {
                'success':True,
                'message':'Upcoming events in the next month:',
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
def filter_events_in_next_3_months(request):
    if request.method == 'GET':
        events = get_events_timeframe(days=90)

        serializer = EventSerializer(events, many=True)

        return Response(
            {
                'success':True,
                'message':'Upcoming events in the next 3 months:',
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )



@api_view(['GET'])
def filter_events_in_next_6_months(request):
    if request.method == 'GET':
        events = get_events_timeframe(days=120)

        serializer = EventSerializer(events, many=True)

        return Response(
            {
                'success':True,
                'message':'Upcoming events in the next 6 months:',
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )



