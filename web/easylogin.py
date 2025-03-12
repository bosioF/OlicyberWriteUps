import requests
import re

url = 'http://easylogin.challs.olicyber.it/'

r = requests.post(url, data={'username': 'admin','password': 'admin', 'totp': '123456'})
print(r.text)