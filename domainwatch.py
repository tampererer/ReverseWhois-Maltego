from MaltegoTransform import *
import requests
import re

me = MaltegoTransform()
whoisinfo = sys.argv[1]

response = requests.get('https://domainwat.ch/search?query=' + whoisinfo + '&type=email')
response = response.text

for fqdn in re.findall(r"<h6 class=\"mb-1\">([^/<>@\'\"]+?)</h6>",response,re.M):
    me.addEntity("maltego.Domain", fqdn)

me.returnOutput()

