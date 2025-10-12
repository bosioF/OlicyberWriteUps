import requests
import json

URL = 'http://flagdownloader.challs.olicyber.it/download/flag/'

flag = []

for i in range(50):
    if i == 0:
        URL = 'http://flagdownloader.challs.olicyber.it/download/flag/0'
        r = requests.get(URL)
        data = r.json()
        flag.append(data['c'])
        NEXT_URL = data['n']
    else:
        if data['c']:
            URL = f'http://flagdownloader.challs.olicyber.it/download/flag/{NEXT_URL}'
            r = requests.get(URL)
            data = r.json()
            flag.append(data['c'])
            NEXT_URL = data['n']
        else:
            final_flag = ''.join(flag)
            print(final_flag)
            exit()
