from MaltegoTransform import *
import requests
import re

me = MaltegoTransform()
whoisinfo = sys.argv[1]

response = requests.get('http://viewdns.info/reversewhois/?q=' + whoisinfo)
response = response.text

for fqdn in re.findall(r"<tr><td>([^/<>@\'\"]+?)</td><td>[0-9]{4}\-[0-9]{2}\-[0-9]{2}</td><td>",response,re.M):
    me.addEntity("maltego.Domain", fqdn)

me.returnOutput()

