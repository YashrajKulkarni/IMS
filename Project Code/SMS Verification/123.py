from twilio.rest import Client
  
# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'ACf91f0f0c2fceb5f8add946fd40b30703'
auth_token = 'deeb3a1ea4b59cc704dc28eec858b023'
  
client = Client(account_sid, auth_token)
  
''' Change the value of 'from' with the number 
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
                              from_='+12072756967',
                              body ='trying twilio Sms service',
                              to ='+919004688228'
                          )
  
print(message.sid)