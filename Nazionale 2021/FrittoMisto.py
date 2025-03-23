import requests

url = 'http://frittomisto.challs.olicyber.it/api/register'

r=requests.post(url, json={
    "username": "wfep0wjofddddddd",
    "password": "uowefh284ddddd",
    "invite": "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09"
})

print(r.text)