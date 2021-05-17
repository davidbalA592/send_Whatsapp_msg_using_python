from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
S_ID = <twilio S-id>
auth = <twilio auth>
client = Client(S_ID,auth)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:<from_number>'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:<to_number>'

client.messages.create(body='Something went wrong: Unauthorised Access!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
