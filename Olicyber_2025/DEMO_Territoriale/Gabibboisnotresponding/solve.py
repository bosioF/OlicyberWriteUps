# non sono state pubblicate queste chall, quindi non posso fixarle rn :(

import requests

url = 'http://gabibbo.xyz'

params={'Content-Type': 'application/json'}
data = {'pos': 10, 'val': 's'}
r = requests.post(url, data=data)

print(r.headers)