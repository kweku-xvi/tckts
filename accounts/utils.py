import os
from dotenv import load_dotenv
from trycourier import Courier

load_dotenv()


client = Courier(auth_token=os.getenv('COURIER_AUTH_TOKEN'))


def email_verification(username:str, email:str, link:str):
    client.send_message(
        message={
            "to": {
            "email": email,
            },
            "template": "HQRFKDHDK84B16GJAQ7PWPFATXS8",
            "data": {
            "username": username,
            "link": link,
            },
        }
    )


def password_reset_mail(username:str, email:str, link:str):
    client.send_message(
        message={
            "to": {
            "email": email,
            },
            "template": "WF7909Y7ZWMNWNNTNNQRHDTBKDF4",
            "data": {
            "username": username,
            "link": link,
            },
        }
    )