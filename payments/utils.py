# import os, string, random, requests
# from dotenv import load_dotenv


# load_dotenv()


# SECRET_KEY = os.getenv('PAYSTACK_SECRET')


# def initialize_transactions(email:str, amount:str, reference:str, ticket_type_id:str):
#     url="https://api.paystack.co/transaction/initialize"

#     headers = {
#         'Authorization':f'Bearer {SECRET_KEY}'
#     }

#     data = {
#         'email':email,
#         'amount':amount,
#         'reference':reference, 
#         'metadata':{
#             'ticket_type_id':ticket_type_id
#         }
#     }

#     response = requests.post(url=url, headers=headers, json=data)

#     if response.status_code == 200:
#         return response.json()['data']['authorization_url']
#     else:
#         return response.json()['message']


# def verify_payment(reference):
#     url="https://api.paystack.co/transaction/verify/{reference}"

#     headers = {
#         'Authorization':f'Bearer {SECRET_KEY}'
#     }

#     response = requests.get(url=url, headers=headers)

#     if response.status_code == 200:
#         return response.json()['data']


import os, string, random, requests
from dotenv import load_dotenv


load_dotenv()


SECRET_KEY = os.getenv('PAYSTACK_SECRET')


def initialize_transactions(email:str, amount:str, reference:str):
    url="https://api.paystack.co/transaction/initialize"

    headers = {
        'Authorization': f'Bearer {SECRET_KEY}'
    }

    data = {
        'email':email,
        'amount':amount,
        'reference':reference
    }

    response = requests.post(url=url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['data']['authorization_url']
    else:
        return response.json()['message']


def verify_payment(reference):
    url="https://api.paystack.co/transaction/verify/{reference}"

    headers = {
        'Authorization': f'Bearer {SECRET_KEY}'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        return response.json()['data']


def generate_id(num:int):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num))


