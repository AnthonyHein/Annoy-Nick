# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Environment variables.
from dotenv import load_dotenv
import os

# Sleep
from time import sleep

load_dotenv()


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

while True:
    message = client.messages \
        .create(
             body='Do you concede?',
             from_='+12013451244',
             to='+17326779062'
         )

    print(message.sid)
    sleep(1)
