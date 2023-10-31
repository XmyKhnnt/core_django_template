from django.conf import settings
import requests
import json
import random


postcodes = [
    "SW1A 1AA",
    "PE35 6EB",
    "CV34 6AH",
    "EH1 2NG"
]


def schedule_api():
    from trycourier import Courier

    try:
        client = Courier(auth_token="pk_prod_6M9PA153W049Y6JS7K8XH161N5YB")

        resp = client.send_message(
            message={
                "to": {
                    "email": "elementalherozerokhent@gmail.com",
                },

                "template": "2092N64GY34CF0QR17ZY71YKGASA",
                "data": {
                    "firstName": "Mereal",
                    "description": "loved",
                    "reminder": "I love you!",
                },
            }
        )

        print(resp['requestId'])

    except:
        pass
