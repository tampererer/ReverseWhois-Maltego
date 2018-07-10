# [ReverseWhois-Maltego] Maltego Local Transforms
Maltego Local Transforms to use the following services.
- DomainEye - https://domaineye.com/
- PrePostSEO - https://www.prepostseo.com/reverse-whois-checker
- Viewdns - https://viewdns.info/

# Prerequisites
- Python 2.7.x + requests, re module

# Setup
- Put domaineye.py, prepostseo.py, viewdns.py and MaltegoTransform.py into your working directory. (e.g. C:\Maltego\Transforms\Whoismind)
- Open Whoismind.mtz to import Maltego configuration.
- The current configuration uses the following directories, so you may have to change them according to your environment. (Maltego -> Transforms -> Transform Manager)  

  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\Whoismind

# Transforms
- [DomainEye] email_to_domain.py
- [PrePostSEO] email_to_domain.py
- [Viewdns] email_to_domain.py
