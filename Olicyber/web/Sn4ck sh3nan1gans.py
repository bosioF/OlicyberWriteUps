import requests

url = 'http://sn4ck-sh3nan1gans.challs.olicyber.it/'

data = {'username': 'bosio', 'password': '123456789'}
r = requests.post(url, data=data)

print(r.headers)