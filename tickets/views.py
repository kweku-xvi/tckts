from .models import TicketType
from .serializers import TicketTypeSerializer, TicketPurchaseSerializer
from  accounts.permissions import IsVerified
from django.shortcuts import render
from programs.models import Event
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
                'message':'Event Not Found'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return event


def get_ticket_type(id:str):
    try:
        ticket_type = TicketType.objects.get(ticket_type_id=id)
    except TicketType.DoesNotExist:
        return Response(
            {
                'success':False,
                'message':'Ticket Type Not Found'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return ticket_type


@api_view(['POST'])
@permission_classes([IsVerified])
def add_ticket_type_view(request, event_id:str):
    if request.method == 'POST':
        current_user = request.user
        event = get_event(id=event_id)

        if current_user != event.organizer and not current_user.is_staff:
            return Response(
                {
                    'success':False,
                    'message':"You do not have the permission to perform this action."
                }, status=status.HTTP_403_FORBIDDEN
            )

        serializer = TicketTypeSerializer(data=request.data)

        if serializer.is_valid():
            if TicketType.objects.filter(event=event, name=serializer.validated_data['name']).exists():
                return Response(
                    {
                        'success':False,
                        'message':'This name is already in use'
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            else:
                serializer.save(event=event)

                return Response(
                    {
                        'success':True,
                        'ticket_type':serializer.data
                    }, status=status.HTTP_201_CREATED
                )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def get_event_ticket_types_view(request, event_id:str): # GET INFO ON TICKET TYPES OF AN EVENT
    if request.method == 'GET':
        event = get_event(id=event_id)

        ticket_types = TicketType.objects.filter(event=event)

        serializer = TicketTypeSerializer(ticket_types, many=True)

        return Response(
            {
                'success':True,
                'message':f'Tickets for {event.name}',
                'ticket_types':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['PUT', 'PATCH'])
@permission_classes([IsVerified])
def update_ticket_type_info_view(request, ticket_type_id:str):
    if request.method == 'PUT' or request.method == 'PATCH':
        current_user = request.user
        ticket_type = get_ticket_type(id=ticket_type_id)

        if current_user != ticket_type.event.organizer and not current_user.is_staff:
            return Response(
                {
                    'success':False,
                    'message':"You do not have the permission to perform this action"
                }, status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = TicketTypeSerializer(ticket_type, data=request.data, partial=True)

        if serializer.is_valid():
            # Only check for name uniqueness if name is being updated
            if 'name' in serializer.validated_data and serializer.validated_data['name'] != ticket_type.name:
                if TicketType.objects.filter(event=ticket_type.event, name=serializer.validated_data['name']).exists():
                    return Response(
                        {
                            'success':False,
                            'message':'This name is already in use.'
                        }, status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                serializer.save()

                return Response(
                    {
                        'success':True,
                        'ticket_type':serializer.data
                    }, status=status.HTTP_201_CREATED
                )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_ticket_type_view(request, ticket_type_id:str):
    if request.method == 'DELETE':
        current_user = request.user
        ticket_type = get_ticket_type(id=ticket_type_id)

        if current_user != ticket_type.event.organizer and not current_user.is_staff:
            return Response(
                {
                    'success':False,
                    'message':"You do not have the permission to perform this action."
                }, status=status.HTTP_403_FORBIDDEN
            )

        ticket_type.delete()

        return Response(
            {
                'success':True,
                'message':'Ticket type deleted successfully'
            }, status=status.HTTP_200_OK
        )


@api_view(['POST'])
@permission_classes([IsVerified])
def purchase_ticket_view(request, ticket_type_id:str):
    if request.method == 'POST':
        ticket_type = get_ticket_type(id=ticket_type_id)
        user = request.user
        event = ticket_type.event

        serializer = TicketPurchaseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user, event=event, ticket_type=ticket_type)

            return Response(
                {
                    'success':True,
                    'message':'Confirm payment',
                    'purchase_details':serializer.data
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )