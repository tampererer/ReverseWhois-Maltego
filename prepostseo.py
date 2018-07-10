from MaltegoTransform import *
import requests
import re

me = MaltegoTransform()
whoisinfo = sys.argv[1]

params ={'q': whoisinfo, 'submit': 'Check Reverse Whois'}
headers = {'Host': 'www.prepostseo.com', 'Origin': 'https://www.prepostseo.com', 'Referer': 'https://www.prepostseo.com/reverse-whois-checker'}
response = requests.post('https://www.prepostseo.com/reverse-whois-checker', data=params)
response = response.text
#print response

for fqdn in re.findall(r"<tr><td>[0-9]{1,2}</td><td>([^/<>@\'\"]+?)</td><td>[0-9]{4}\-[0-9]{2}\-[0-9]{2}</td><td>",response,re.M):
    me.addEntity("maltego.Domain", fqdn)

me.returnOutput()

