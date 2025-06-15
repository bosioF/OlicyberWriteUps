import requests

url1 = 'http://spider.challs.olicyber.it/supe3s3cretf0lder/flag1.txt'
url2 = 'http://spider.challs.olicyber.it/standardNonSecretFolder/flag2.txt'

def fetch_flag_part(url):
        response = requests.get(url, timeout=5)
        return response.text.strip()

part1 = fetch_flag_part(url1) 
part2 = fetch_flag_part(url2) 

if part1 and part2:
    part1_cleaned = part1.split('\n')[0] 
    full_flag = part1_cleaned + part2 
    print(f"flag: {full_flag}")
else:
    print("error")
