import requests
import re

URL = "http://prettyplease.challs.olicyber.it"
r = requests.post(URL, data={'how': 'pretty please'})
flag = re.search(r'flag{.*}', r.text).group(0)
print(flag)