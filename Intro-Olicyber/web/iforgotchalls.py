import requests

url = 'http://iforgot.challs.olicyber.it/'
r = requests.head(url)
print(r.headers)