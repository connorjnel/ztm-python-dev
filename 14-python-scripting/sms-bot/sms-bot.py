from twilio.rest import Client

account_sid = "65s1df651sdf1g6sd51f"
auth_token = "[32sd1f321sdf]"

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="+123456789",
    body="Test",
    to="+123456789",
)

print(message.sid)
