from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
S_ID = "AC81301a8f1df45056589c4032856e2c58"
auth = "82699285cc0f6690b48289b7472fa3f0"
client = Client(S_ID,auth)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+919094458858'

client.messages.create(body='Something went wrong: Unauthorised Access!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
