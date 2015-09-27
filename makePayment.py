import simplify
from Person import PersonInfo
from Person import *
import time

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




