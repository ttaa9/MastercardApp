import simplify
from Person import PersonInfo
from Person import *

# Settings
NAME = "bob@hotmail.com"
AMOUNT = "979"

# Set Keys
simplify.public_key = "sbpb_ZjU3YTNmMjItNDU3ZC00MWI1LTk4YTktZjkzZmQ2Y2ZiNjIw"
simplify.private_key = "VJcLMAVGrrhn7QbJPkUMONEB7rOz2+9OUqf4q3CL/xl5YFFQL0ODSXAOkNtXTToq"

# Read in person's info
p = PersonInfo(NAME)

# Create payment
payment = simplify.Payment.create({
       "card" : {
            "number": p.cardNum,
            "expMonth": p.expMonth,
            "expYear": p.expYear,
            "cvc": p.cvc
        },
        "amount" : AMOUNT,
        "description" : "CharityDonation",
        "currency" : "USD"
})

# Print approval status
print payment
if payment.paymentStatus == 'APPROVED':
    print "Payment approved"

# Add to the transaction history





