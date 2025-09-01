import requests
import re
from selenium import webdriver

url = 'http://infinite.challs.olicyber.it/'

r = requests.get(url).text
eq = str(re.findall(r'<p>(.*?)</p>', r))
line = eq.split(' ')
print(eq)

if 'Quante' in line[0]:
    x = 0
    letter = line[1].replace('"', '')
    word = line[6].translate(str.maketrans('', '', '"?\']'))
    c = word.count(letter)

#DA FINIRE