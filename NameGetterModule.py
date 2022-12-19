from twilio.rest import Client

namenumdict = {'name':"",'number':"",'store':""}

def getname(number):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = [SID]
    auth_token = [TOKEN]
    client = Client(account_sid, auth_token)

    phone_number = client.lookups \
                         .phone_numbers(number) \
                         .fetch(type=['caller-name'])

    namenumdict['name'] = phone_number.caller_name['caller_name']
    namenumdict['number'] = number
    namenumdict['store'] = "WR"
    print(namenumdict['name'])
    return namenumdict['name']

if __name__=='__main__':
    getname()
