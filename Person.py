import os,sys,collections


# Settings
datapath = "Data"
transacHistoryAffixes = ["th-", ".txt"]
settingsAffixes = ["settings-", ".txt"]
accountsFile = "accounts.csv"
mastercardApiPythonPath = "mc_python_api/mastercard-api-python"

# Global Variables and Methods
levels = collections.OrderedDict([(0,"Giver"), (20,"Good Samaritan"), 
	(100,"Beginner Philanthropist"), (500,"Advanced Philanthropist"), 
	(1000,"Angel"), (2500,"Healer of Woe"), (4000,"Bringer of Light"), 
	(1000000,"Saint")])

def getLevel(amount):
	for i,key in enumerate(levels.keys()):
		if amount < key: return levels.values()[i-1]
	return "DEFAULT"
# Account class
class PersonInfo: #(object):
	
	# Constructor for standard existing user login.
	def __init__(self, username):
		# Actual creation
		fs = os.path.join(datapath, settingsAffixes[0] + username + settingsAffixes[1])
		fth = os.path.join(datapath, transacHistoryAffixes[0] + username + transacHistoryAffixes[1])
		if os.path.isfile(fs):
			# Read in settings
			i=0
			f = [p.strip() for p in open(fs,"r").readlines()]
			self.username = f[i]
			self.cardNum = f[i+1]
			self.totalDonations = f[i+2]
			self.firstName = f[i+3]
			self.lastName = f[i+4]
			self.gender = f[i+5]
			self.expMonth = f[i+6]
			self.expYear = f[i+7]
			self.cvc = f[i+8]
			# Read in transaction history (line: charityName,date,amount)
			f2 = open(fth,"r").readlines()
			temp = [ k.strip().split(",") for k in f2]
			self.transactionHistory = [ [t[0],t[1],float(t[2])] for t in temp ]
			self.level = getLevel(self.getTotalDonations())
		else:
			print(fs)
			assert False, "New account Capability Turned Off"
			# Fill in defaults
			self.username = username
			self.cardNum = -1
			self.totalDonations = 0
			self.firstName = ""
			self.lastName = ""
			self.transactionHistory = []
			self.gender = "Not Set"
			self.expMonth = -1
			self.expYear = -1
			self.cvc = -1
			self.level = getLevel(self.getTotalDonations())
			# Write a new file
			self.write()

	def addTransaction(self,amount,charityName,dateString):
		self.transactionHistory.append([charityName,dateString,float(amount)])
		self.totalDonations = self.getTotalDonations()
		self.level = getLevel(self.getTotalDonations())
		self.write()
		with open('Data/bt-bob@hotmail.com.csv','a') as o:
			o.write(charityName+','+dateString+','+str(amount)+',0\n')
			o.close()

	# TODO: Check validity
	def setCardNum(self, cardnum):
		# Imports
#		sys.path.insert(0, mastercardApiPythonPath)
#		p = 'mc_python_api.mastercard-api-python.Common'
#		from mc_python_api.mastercard-api-python.common.Environment import environment
#		from services.lost_stolen import loststolenservice
	#	print("hi")
		# Check validity

		# Set card Number
		self.cardNum = cardnum

	def toSettingsString(self):
		return "\n".join([self.username, str(self.cardNum),
			str(self.getTotalDonations()), self.firstName, self.lastName,self.gender,
			str(self.expMonth), str(self.expYear), str(self.cvc)])

	def makeTransactionHistoryString(self):
		ss = [ str(k[0]) + "," + str(k[1]) + "," + str(k[2]) for k in self.transactionHistory ]
		return "\n".join(ss)

	# Writes "person" object to files
	def write(self):
		# Write Settings
		fs = os.path.join(datapath, settingsAffixes[0] + self.username + settingsAffixes[1])
		fth = os.path.join(datapath, transacHistoryAffixes[0] + self.username + transacHistoryAffixes[1])
		setFile = open(fs,"w")
		setFile.write(self.toSettingsString())
		setFile.close()
		thFile = open(fth,"w")
		thFile.write(self.makeTransactionHistoryString())
		thFile.close()

	def getTotalDonations(self):
		return sum( [k[2] for k in self.transactionHistory] )

	@staticmethod
	def firstDateStringIsGreater(s1,s2):
		m1,d1,y1 = s1.split("/")
		m2,d2,y2 = s2.split("/")
		if y1>y2: return True
		if m1>m2: return True
		if d1>d2: return True
		return False

	def getPercentageToNextLevel(self):
		total = self.getTotalDonations()
		for i,key in enumerate(levels.keys()):
			if total < key: 
				nextLevAmount = levels.keys()[i]
				k = float(total)/float(nextLevAmount)*100
				return '{00:.{1}f}'.format(k,1)
			#	return levels.values()[i-1]
		return "DEFAULT"

	def getNameOfNextLevel(self):
		for i,key in enumerate(levels.keys()):
			if self.getTotalDonations() < key: return levels.values()[i]
		return "DEFAULT"

	def generateDonationTable(self):
		chars = []
		lastDate = []
		lastAmount = []
		lifetimeTotals = []
		for e in self.transactionHistory:
			if e[0] in chars:
				ind = chars.index(e[0])
				if PersonInfo.firstDateStringIsGreater(e[1],lastDate[ind]): # current no greater
					lastDate[ind] = e[1]
					lastAmount[ind] = e[2]
				lifetimeTotals[ind] += e[2] 
			else:
				chars.append(e[0])
				lastDate.append(e[1])
				lastAmount.append(e[2])
				lifetimeTotals.append(e[2])
		s = ""
		for i,c in enumerate(chars):
			s += "<tr>"
			s += "<td>"+str(c)+"</td>"
			s += "<td>"+str(lastDate[i])+"</td>"
			s += "<td>$"+str(lastAmount[i])+"</td>"
			s += "<td>$"+str(lifetimeTotals[i])+"</td>"
			s += "</tr>"
		print(s)
		return s

	def genBankTransTable(self):
		with open('Data/bt-bob@hotmail.com.csv','r') as f:
			table=""
			for line in f:
				parts = line.split(',')
				table += "<tr>"
				table += "<td>"+parts[0]+"</td>"
				table += "<td>"+parts[1]+"</td>"
				table += "<td>$"+parts[2]+"</td>"
				table += "<td>$"+parts[3]+"</td>"
				table += "</tr>"
		return table

	def genUpcomingDonation(self):
		with open('Data/bt-bob@hotmail.com.csv','r') as f:
			total=0
			for line in f:
				parts = line.split(',')
				total+=float(parts[3])
		return total

### Main Method (test) ###




