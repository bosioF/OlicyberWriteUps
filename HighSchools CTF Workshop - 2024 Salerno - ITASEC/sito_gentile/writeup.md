# ITASEC24 - CTF Workshop Salerno

## Sito Gentile

### Challenge description
```
Dove la gentilezza diventa un'abitudine quotidiana e un'ispirazione per un mondo migliore.

Sito: http://sitogentile.challs.olicyber.it
```
---
## Solve

When the request is made to `/talk`, the server responds with the message, but also includes the flag in the headers.
Specifically, one character for each header named `X-Flag-N`, where N is the character index.

## Exploit

```python
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
```

By running the script, we obtain the flag:
```
ITASEC{th3_1nt3rn3t_w0rk5_1n_my5t3r10us_w4ys}
```