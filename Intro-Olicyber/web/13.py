from re import findall

import  requests
from bs4 import BeautifulSoup

url = 'http://web-13.challs.olicyber.it/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
flag = soup.find_all('span')
letters = ''.join([element.text for element in flag])
print("flag" + "{" + letters + "}")