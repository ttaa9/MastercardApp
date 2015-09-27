import simplify
from Person import PersonInfo
from Person import *
import time
import requests
import xml.etree.ElementTree as et

# Settings
NAME = "bob@hotmail.com"
AMOUNTS = ["332", "431"]
CHARITY_NAMES = ["Fukushima Rebuilding Fund" , "Japan Tsunami Relief"]


def makePayment(name,amount,charityName):
    # Set Keys
    simplify.public_key = "sbpb_ZjU3YTNmMjItNDU3ZC00MWI1LTk4YTktZjkzZmQ2Y2ZiNjIw"
    simplify.private_key = "VJcLMAVGrrhn7QbJPkUMONEB7rOz2+9OUqf4q3CL/xl5YFFQL0ODSXAOkNtXTToq"
    # Read in person's info
    p = PersonInfo(name)

    # Check for Fraud/Stolen
    xml = '''<?xml version='1.0' encoding='utf-8'?>'''
    body = '''<AccountInquiry><AccountNumber>'''+p.cardNum+'''</AccountNumber></AccountInquiry>'''
    headers = {'content-type': 'application/xml', 'content-length': '{length}'}
    path = '/fraud/loststolen/v1/account-inquiry?Format=XML'
    results = requests.put('http://dmartin.org:8026/fraud/loststolen/v1/account-inquiry?Format=XML',
        data=body,headers=headers)
    print results.text
    tree = et.fromstring(results.text)
    for elem in tree.iter():
        if elem.tag == "Listed":
            if elem.text == "true":
                print "Aborting transaction - Reported Card!"
                return
    print "Passed check" # May be due to server non-recognition

    # Create payment
    payment = simplify.Payment.create({
           "card" : {
                "number": p.cardNum,
                "expMonth": p.expMonth,
                "expYear": p.expYear,
                "cvc": p.cvc
            },
            "amount" : amount,
            "description" : "Donation to " + charityName,
            "currency" : "USD"
    })
    # Print approval status
    print payment
    if payment.paymentStatus == 'APPROVED':
        print "Payment approved"
    # Add to the transaction history
    p.addTransaction(amount,charityName,(time.strftime("%m/%d/%Y")))

for k in zip(AMOUNTS,CHARITY_NAMES):
    makePayment(NAME,k[0],k[1])




