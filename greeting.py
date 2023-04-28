import os
from twilio.rest import Client
import datetime

# Set the Twilio credentials
account_sid = 'AC4b3eabdf6640a6361be680bf31d85af6'
auth_token = '7e99f0cf50cd27ee4db0f5266acb0f68'
client = Client(account_sid, auth_token)

# Set the list of friends with their details
friends = [
    {
        'name': 'Samuel',
        'phone': '+2348064239965',
        'birthday': '2023-04-28'
    }
]

# Get the current date
today = datetime.datetime.today().strftime('%Y-%m-%d')

# Loop through the friends list and send the messages
for friend in friends:
    if friend['birthday'] == today:
        message = client.messages.create(
            body=f'Happy Birthday, {friend["name"]}!',
            from_='+16203839477',
            to=friend['phone']
        )
        print(f'Message sent to {friend["name"]} ({friend["phone"]}). Message ID: {message.sid}')
