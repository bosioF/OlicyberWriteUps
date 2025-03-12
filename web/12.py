import requests
from bs4 import BeautifulSoup

url = "http://web-12.challs.olicyber.it/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    if len(paragraphs) >= 2:
        second_paragraph = paragraphs[1].text
        print("La flag è:", second_paragraph)
    else:
        print("Non ci sono abbastanza paragrafi nella pagina.")
else:
    print(f"Errore nel download della pagina. Codice HTTP: {response.status_code}")
