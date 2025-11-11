import requests
import re

URL = "http://was-it-a-flag.challs.olicyber.it/flag.php"

r = requests.post(URL, data={"password": "gabibbo"}, allow_redirects=False)

match = re.search(r"flag\{[^\}]+\}", r.text, re.IGNORECASE)
if match:
    print(match.group(0))