            # app.py
from flask import Flask, request, jsonify
from twilio.rest import Client
import datetime
# import os
import smtplib
# import requests
from NameGetterModule import getname
from GmailerModule import sendanemail
from XMLLeadMakerModule import makexml
#from texttostring import maketextstring

account_sid = [SID]
auth_token = [TOKEN]
client = Client(account_sid, auth_token)

app = Flask(__name__)



# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>The server works.  Good job, Bob.</h1>"


@app.route('/textbot/', methods=['GET'])
def finalish():
    custnum = request.args.get("custnum")
    custname = request.args.get("custname")
    print(f"Customer Name: {custname}, Customer Number: {custnum}!")

    from NameGetterModule import getname
    name = getname(custnum)
    print('namegetter done')
    from XMLLeadMakerModule import makexml
    xmltomail = makexml(name,custnum)

    from GmailerModule import sendanemail
    xmltomail = str(xmltomail)
    sendanemail(xmltomail)

    return "Ugh..."



'''
    custname2 = getname(custname)
    print(custname2)
    xmlcontent = makexml(custname2,custnum)
    print(xmlcontent)
    emailabletext = maketextstring()
    print(emailabletext)
    sendanemail(emailabletext)
    return "it worked, i think"
'''






if __name__=='__main__':
    app.run()
