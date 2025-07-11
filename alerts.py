from twilio.rest import Client

def send_alert (phone_number, message):
    try:
        account_sid = 'AC2721f64f695bdb55e41f4feac6e3d23c'
        auth_token = '13d82910665acd3d635dfee5b73b33cf'
        twilio_number = '+14786075163'
    
        client = Client(account_sid, auth_token)
        message= client.messages.create(
            body=message,
            from_ = twilio_number,
            to= phone_number
        )

        print("sms sent successfully")
    except Exception as e:
        print ("eoor sending sms:", e)

    