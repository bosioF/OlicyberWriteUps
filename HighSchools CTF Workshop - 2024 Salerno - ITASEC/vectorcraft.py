import requests
import re

url = 'http://vectorcraft.challs.olicyber.it/logo.svg'
r = requests.get(url)
flag = re.findall(r'<!--(.*?)-->', r.text, re.DOTALL)
print(flag)