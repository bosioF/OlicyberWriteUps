"""from requests import Session

url_flag = 'http://web-11.challs.olicyber.it/flag_piece'
url_login = 'http://web-11.challs.olicyber.it/login'

session = Session()

headers = {'Content-Type': 'application/json'}
login_payload = {'username': 'admin', 'password': 'admin'}

login_response = session.post(url_login, headers=headers, json=login_payload)
if login_response.status_code != 200:
    print(f"Login failed: {login_response.status_code} {login_response.text}")
    exit()

try:
    csrf_token = login_response.json().get("csrf")
    session_cookie = login_response.cookies.get_dict()
    #print(session_cookie)
    if not csrf_token:
        print("CSRF token not found in login response.")
        exit()
    if not session_cookie:
        print("Session cookie not found in login response")
        exit()
except ValueError:
    print("invalid JSON in login response.")
    exit()

flag_pieces = []

for index in range(4):
    cookies = {'csrf': csrf_token,**session_cookie}
    if index == 0:
        print(session_cookie)
    params = {'index': index}

    try:
        response = session.get(url_flag, cookies=cookies, params=params)
        if response.status_code != 200:
            print(f"failed to fetch flag piece at index {index}: {response.status_code}")
            continue

        data = response.json()
        flag_piece = data.get("flag")
        if not flag_piece:
            print(f"flag piece missing at index {index}.")
            continue

        flag_pieces.append(flag_piece)
        csrf_token = data.get("csrf")

    except ValueError:
        print(f"invalid JSON response at index {index}.")
    except Exception as e:
        print(f"error fetching flag piece at index {index}: {e}\n")

flag = ''.join(flag_pieces)
print(f"flag: {flag}")
"""

import requests

login = "http://web-11.challs.olicyber.it/login"
flag = "http://web-11.challs.olicyber.it/flag_piece"

req = requests.session()

json_data = req.post(login, json={"username":"admin", "password":"admin"}).json()

csrf = json_data["csrf"]


for i in range(4):
    r = req.get(flag, params={"index": i,"csrf": csrf})
    json_data = r.json()
    csrf = json_data["csrf"]
    print(json_data["flag_piece"], end="")
