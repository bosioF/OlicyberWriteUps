import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = url = "http://web-15.challs.olicyber.it/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

resources = []

image = soup.find_all('img', src=True)
for img in image:
    resources.append(urljoin(base_url, img['src']))
css_files = soup.find_all('css', src=True)
for css in css_files:
    resources.append(urljoin(base_url, css['src']))
scripts = soup.find_all('script', src=True)
for  scr in scripts:
    resources.append(urljoin(base_url, scr['src']))

for resource in resources:
    print(resource.strip())

r = requests.get(resource).text
soup = BeautifulSoup(r, 'html.parser')
flag = None
for text in soup.stripped_strings:
    if "flag{" in text:
        flag = text.strip()
        break

if flag:
    print(f"Flag trovata: {flag}")
