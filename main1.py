from twilio.rest import Client

# Replace these with your actual Twilio credentials
account_sid = 'AC0cf8d6de6944b2a101e88335c3cd5cfe'
auth_token = '7df147a7e6d594f5cd6c7a512d0e084e'
twilio_phone_number = '+923008147447'  # Replace with your Twilio phone number
recipient_phone_number = '+923120614727'  # Replace with the recipient's phone number
message_body = "Kya haal ha"  # Replace with your desired message

def send_sms(to_phone_number, from_phone_number, message):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=to_phone_number,
            from_=from_phone_number,
            body=message
        )
        print(f"SMS sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

if __name__ == "__main__":
    send_sms(recipient_phone_number, twilio_phone_number, message_body)
