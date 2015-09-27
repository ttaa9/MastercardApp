#!C:\Users\Tristan\Anaconda\python.exe -u
 
print "Content-type: text/html"
print
print "<title>Test CGI</title>"
print "<p>Hello World TEST!</p>"

import cgi
 
form = cgi.FieldStorage()
 
val1 = form.getvalue('first')
val2 = form.getvalue('last')
 
print """ Hello my name is %s %s
</body></html>""" % (val1, val2)

#"""Content-type: text/html
#<html><head><title>Test URL Encoding</title></head><body>
""" Hello my name is %s %s
</body></html>""" % (val1, val2)