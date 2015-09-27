#sys.path.insert(0, mastercardApiPythonPath)
#		p = 'mc_python_api.mastercard-api-python.Common'
#		from mc_python_api.mastercard-api-python.common.Environment import environment
#		from services.lost_stolen import loststolenservice
import sys
import httplib
import urllib
import requests
import xml.etree.ElementTree as et

xml = '''<?xml version='1.0' encoding='utf-8'?>'''
body = '''<AccountInquiry><AccountNumber>5343434343434343</AccountNumber></AccountInquiry>'''
body = '''<AccountInquiry><AccountNumber>5555555555554444</AccountNumber></AccountInquiry>'''

headers = {'content-type': 'application/xml', 'content-length': '{length}'}
path = '/fraud/loststolen/v1/account-inquiry?Format=XML'

results = requests.put('http://dmartin.org:8026/fraud/loststolen/v1/account-inquiry?Format=XML',
	data=body,headers=headers)
print results.text
tree = et.fromstring(results.text)
#root = tree.getroot()
for elem in tree.iter():
    print elem.tag, elem.attrib, elem.text

'''
a = httplib.HTTPConnection('dmartin.org',8026)
a.request('PUT',path,body=body,headers=headers)#,body=body,headers=headers)
c = a.getresponse()
print c.read()
print c.status
'''
'''
import urllib2
import sys
import httplib

xml = '''<?xml version='1.0' encoding='utf-8'?>'''
body = '''<AccountInquiry><AccountNumber>5343434343434343</AccountNumber></AccountInquiry>'''
headers = {'content-type': 'application/xml', 'content-length': '{length}'}
path = '/fraud/loststolen/v1/account-inquiry?Format=XML'
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://dmartin.org:8026/fraud/loststolen/v1/account-inquiry?Format=XML', data=body)
request.add_header('content-Type', 'application/xml')
#request.add_header('content-length', 8) #'{length}')
request.get_method = lambda: 'PUT'
#url = opener.open(request)
response = urllib2.urlopen(request)
'''
'''
connection = httplib.HTTPConnection('dmartin.org',8026) # httplib.HTTPConnection('1.2.3.4:1234')
#body_content = 'BODY CONTENT GOES HERE'
connection.request('PUT', path, body) #_content)
result = connection.getresponse()
'''
'''
PUT
https://api.mastercard.com/fraud/loststolen/v1/account-inquiry?Format=XML

Headers:
content-type: application/xml
content-length: {length}

Body:
<AccountInquiry>
	<AccountNumber>5343434343434343</AccountNumber>
</AccountInquiry>
'''

