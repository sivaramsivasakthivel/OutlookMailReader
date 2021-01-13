import os
from twilio.rest import Client

import credentials

print(credentials.Twilio_Sid)
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ[credentials.Twilio_Sid]
#auth_token = os.environ[credentials.Auth_token]

def send_twil_msg(content): 
    """ content is the body. Replace the Credentials"""
    client = Client(credentials.Twilio_Sid, credentials.Auth_Token)

    message = client.messages \
                    .create(
                        body=content,
                        from_= credentials.From_Number,
                        to= credentials.To_Number
                    )

    print(message.sid)


#send_twil_msg("Hello")

