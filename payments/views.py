# import json
# from .models import TicketPurchase
# from .serializers import TicketQuantitySerializer
# from .utils import initialize_transactions, generate_payment_id, verify_payment
# from accounts.models import User
# from accounts.permissions import IsVerified
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from tickets.models import TicketType
# from tickets.views import get_ticket_type


# @api_view(['POST'])
# @permission_classes([IsVerified])
# def buy_tickets(request, ticket_type_id:str):
#     if request.method == 'POST':
#         user = request.user
#         email = user.email

#         ticket_type = get_ticket_type(id=ticket_type_id)

#         serializer = TicketQuantitySerializer(data=request.data)        

#         if serializer.is_valid():

#             transaction = initialize_transactions(email=email, amount=str(ticket_type.price * serializer.validated_data['quantity'] * 100), reference=generate_payment_id(15), ticket_type_id=ticket_type_id)

#             return Response(
#                 {
#                     'success':True,
#                     'transaction_url':transaction
#                 }, status=status.HTTP_200_OK
#             )


# @api_view(['POST'])
# def payment_webhook(request): # ERROR
#     if request.method == 'POST':
#         payload = json.loads(request.body)

#         event = payload['event']
#         data = payload['data']

#         if event == 'charge.success':
#             reference = data['reference']

#             user=User.objects.get(email=data['customer']['email']),
#             ticket_type=TicketType.objects.get(ticket_type_id=data['metadata']['ticket_type_id']),
#             event=ticket_type.event,
#             amount=data['amount'] / 100
#             purchased_at=data['paid_at']

#             TicketPurchase.objects.create(
#                 user=user,
#                 ticket_type=ticket_type,
#                 event=event,
#                 amount=amount,
#                 quantity=ticket_type.price,
#                 purchased_at=purchased_at,
#                 purchase_date=purchased_at.date()
#             )

#         return Response(
#             {
#                 'success':True,
#                 'reference_id':reference
#             }, status=status.HTTP_200_OK
#         )


import json
from .models import Payment
from .utils import initialize_transactions, generate_id
from accounts.permissions import IsVerified
from accounts.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from tickets.models import TicketPurchase


def get_specific_purchase(id:str):
    try:
        purchase = TicketPurchase.objects.get(purchase_id=id)
    except TicketPurchase.DoesNotExist:
        return Response(
            {
                'success':True,
                'message':'Ticket Purchase Not Found'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return purchase


@api_view(['POST'])
@permission_classes([IsVerified])
def buy_tickets(request, purchase_id:str):
    if request.method == 'POST':
        email = request.user.email
        purchase = get_specific_purchase(id=purchase_id)

        transaction = initialize_transactions(email=email, amount=str(purchase.total_amount() * 100), reference=generate_id(20))

        return Response(
            {
                'success':True,
                'transaction_url':transaction
            }, status=status.HTTP_200_OK
        )


@api_view(['POST'])
@authentication_classes([])
def payment_webhook(request):
    payload = json.loads(request.body)

    event = payload['event']
    data = payload['data']

    if event == 'charge.success':
        reference = data['reference']

        payment = Payment.objects.create(
            payment_id=reference,
            amount=data['amount'] / 100,
            user=User.objects.get(email=data['customer']['email']),
            paid_at=data['paid_at']
        )
    
    return Response(
        {
            'success':True,
            'reference_id':reference
        }, status=status.HTTP_200_OK
    )