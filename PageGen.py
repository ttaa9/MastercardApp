#!C:\Users\Tristan\Anaconda\python.exe -u

from Person import PersonInfo
from Person import *
import os,sys
import cgi
 
### Retrieve CGI Values ###
form = cgi.FieldStorage()
val1 = form.getvalue('first')
val2 = form.getvalue('last')
###########################


### Method Definitions ###
# Validate account
def isValidUP(username,password):
	accFile = open(os.path.join(datapath,accountsFile),"r").readlines()
	for pair in accFile:
		u,p = pair.strip().split(",")
		if u==username and p==password: return True
	return False

#





#####################
# CGI Generate Page #
#####################

### Authentication Failed ###
if not isValidUP(val1,val2):
	print "Content-type: text/html"
	print
	print "<title>Test CGI</title>"
	print """ Invalid U+P: %s %s
	</body></html>""" % (val1, val2)

### Authentication Worked ###
else:
	print "Content-type: text/html"
	print
	print "<title>Test CGI</title>"
	print """ Valid U+P: %s %s
	</body></html>""" % (val1, val2)