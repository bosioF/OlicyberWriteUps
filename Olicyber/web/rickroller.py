import requests

url = 'http://roller.challs.olicyber.it/get_flag.php'
r = requests.get(url, allow_redirects=False)
print(r.text)