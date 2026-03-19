import requests

url = 'http://gabibbo-says.challs.olicyber.it/'

params = {'gabibbo': 'angry'}
r = requests.post(url, data=params)
print(r.text)