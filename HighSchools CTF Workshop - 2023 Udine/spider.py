from bs4 import BeautifulSoup
import requests

url = 'http://spider.challs.olicyber.it/'
visited = set()


def find_flag(url):
    queue = [url]
    while queue:
        current_url = queue.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)

        response = requests.get(current_url)
        print(f"richiesta a {current_url}, stato: {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')

        h1_tag = soup.find('h1')
        if h1_tag and 'flag' in h1_tag.text.lower():
            print(f"flag trovata in {current_url}: {h1_tag.text.strip()}")
            return

        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            if link.startswith('/'):
                link = f'http://spider.challs.olicyber.it{link}'
            if link not in visited:
                queue.append(link)


find_flag(url)
