import requests

url = 'http://headache.challs.olicyber.it/'

r = requests.get(url)

print(r.headers)