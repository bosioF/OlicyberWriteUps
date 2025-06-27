import requests

url = 'http://sitogentile.challs.olicyber.it/talk'

r = requests.get(url)

flag_parts = {}

for key, value in r.headers.items():
    if key.startswith('X-Flag-'):
        index = int(key.split('-')[-1])
        flag_parts[index] = value

flag = ''.join(flag_parts[i] for i in sorted(flag_parts))
print(flag)
