from MaltegoTransform import *
import requests
import re

me = MaltegoTransform()
email = sys.argv[1]
pattern = re.compile("(.+)@(.+)")
m = pattern.search(email)
username = m.group(1).encode("base64").strip()
domain = m.group(2)

response = requests.get('http://www.whoismind.com/email/' + username + '-' + domain + '.html')
response = response.text

for fqdn in re.findall(r"Whois data\">(.*?)</a><br />",response,re.M):
    me.addEntity("maltego.Domain", fqdn)

me.returnOutput()

