import os,sys,collections

# Settings
datapath = "../Data"
transacHistoryAffixes = ["th-", ".txt"]
settingsAffixes = ["settings-", ".txt"]
accountsFile = "accounts.csv"

# Global Variables and Methods
levels = collections.OrderedDict([(0,"Kind Person"), (20,"Good Samaritan"), 
	(100,"Beginner Philanthropist"), (500,"Advanced Samaritan"), 
	(1000,"Angel")])

def getLevel(amount):
	for i,key in enumerate(levels.keys()):
		if amount < key: return levels.values()[i-1]

print("reading")

# Account class
class PersonInfo: #(object):
	
	# Constructor for standard existing user login.
	def __init__(self, username):
		# Actual creation
		fs = os.path.join(datapath, settingsAffixes[0] + username + settingsAffixes[1])
		fth = os.path.join(datapath, transacHistoryAffixes[0] + username + transacHistoryAffixes[1])
		if os.path.isfile(fs):
			# Read in settings
			self.username = username
			f = open(fs,"r").readlines()
			self.cardNum = f[0]
			self.totalDonations = f[1]
			self.level = getLevel(self.totalDonations)
			self.firstName = f[2]
			self.lastName = f[3]
			# Read in transaction history (line: charityName,amount)
			f2 = open(fth,"r").readlines()
			temp = [ k.strip().split(",") for k in f2]
			self.transactionHistory = [ [t[0], float(t[1])] for t in temp ]
		else:
			assert False, "New account Capability Turned Off"
			# Fill in defaults
			self.username = username
			self.cardNum = -1
			self.totalDonations = 0
			self.firstName = ""
			self.lastName = ""
			self.level = getLevel(self.totalDonations)
			self.transactionHistory = {}
			# Write a new file
			self.write()

	# TODO: Check validity
	def setCardNum(self, cardnum):
		# Check validity
		# ...............
		# Set card Number
		self.cardNum = cardnum

	def toSettingsString(self):
		return "\n".join([self.username, str(self.cardNum),
			str(self.totalDonations), self.firstName, self.lastName])

	def makeTransactionHistoryString(self):
		ss = [ str(k[0]) + "," + str(k[1]) for k in self.transactionHistory ]
		return "\n".join(ss)

	# Writes "person" object to files
	def write(self):
		# Write Settings
		fs = settingsAffixes[0]+self.username+settingsAffixes[1]
		fth = transacHistoryAffixes[0]+self.username+transacHistoryAffixes[1]
		setFile = open(fs,"w")
		setFile.write(self.toSettingsString())
		setFile.close()
		thFile = open(fth,"w")
		thFile.write(self.makeTransactionHistoryString())
		thFile.close()




### Main Method (test) ###




