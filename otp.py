import twilio.rest as tr

client = tr.Client('SSID','Token')
client.messages.create(from_='twilio', to=9392550548, body = 'Your otp is 9999')

