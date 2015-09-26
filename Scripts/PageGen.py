from Person import PersonInfo
import os,sys

# Validate account
def isValidUP(username,password):
	accFile = open(os.path.join(accountsFile),"r").readlines()
	for pair in accFile:
		u,p = pair.strip().split(",")
		if u==username && p==password: return True
	return False








