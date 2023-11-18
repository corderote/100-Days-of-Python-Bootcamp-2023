# This class is responsible for sending notifications with the deal flight details.
import smtplib
from twilio.rest import Client

TWILIO_ID = "YOUR_TWILIO_ACCOUNT_ID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR_TWILIO_VIRTUAL_NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR_TWILIO_VERIFIED_NUMBER"

# Change this to the email provider smtp address.
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASSWORD"


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

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
