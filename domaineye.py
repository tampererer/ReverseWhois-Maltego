from MaltegoTransform import *
import requests
import re

me = MaltegoTransform()
whoisinfo = sys.argv[1]

response = requests.get('https://domaineye.com/reverse-whois/' + whoisinfo)
response = response.text

for fqdn in re.findall(r"<a href = 'https://domaineye.com/similar/[^/<>@\'\"]+'>(.*?)</a>",response,re.M):
    me.addEntity("maltego.Domain", fqdn)

me.returnOutput()

