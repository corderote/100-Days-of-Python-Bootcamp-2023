# This class is responsible for sending notifications with the deal flight details.

from twilio.rest import Client

TWILIO_ID = "YOUR_TWILIO_ACCOUNT_ID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR_TWILIO_VIRTUAL_NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR_TWILIO_VERIFIED_NUMBER"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
