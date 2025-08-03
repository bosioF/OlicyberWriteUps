import requests

url = 'https://lingua.challs.olicyber.it/'

headers = {'Content-type': 'application/gabibbo'}
r = requests.get(url, headers=headers)
print(r.text)