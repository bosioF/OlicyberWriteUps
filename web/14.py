import re
import requests
from bs4 import BeautifulSoup, Comment

url = 'http://web-14.challs.olicyber.it/'

r = requests.get(url)
html_content = r.text

soup = BeautifulSoup(html_content, 'html.parser')

comment = soup.find_all(string=lambda text: isinstance(text, Comment))

for comments in comment:
    print(comments.strip())




