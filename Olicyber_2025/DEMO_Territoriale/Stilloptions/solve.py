import requests

url = 'https://stilloptions.challs.olicyber.it'

data = {'secret': 'yhrwlduoasd'}
r = requests.options(url, json=data)

print(r.headers, "\n" + r.text)