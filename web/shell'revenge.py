import requests

url = 'http://shellrevenge.challs.olicyber.it'

r = requests.get(url)

print(r.text)