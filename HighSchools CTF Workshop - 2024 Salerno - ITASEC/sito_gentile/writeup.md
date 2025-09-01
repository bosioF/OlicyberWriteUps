# Hidden Headers Challenge – Writeup

## Challenge Description
The flag is hidden inside the HTTP response headers of a given endpoint. Each part of the flag is stored in a custom header, and the solver must reconstruct it in the correct order.

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
````

## Code Analysis

1. **Target URL**
   The exploit sends a GET request to the challenge endpoint.

2. **Inspecting Headers**

   * The response contains custom headers prefixed with `X-Flag-`.
   * Each such header stores a part of the flag.
   * The number after the dash (`X-Flag-1`, `X-Flag-2`, …) indicates the correct order.

3. **Reconstructing the Flag**

   * The script extracts all headers that begin with `X-Flag-`.
   * It parses the index from the header name and stores the value.
   * Finally, it concatenates the values in ascending index order.

4. **Output**
   The complete flag is printed as a single string.

## Exploitation Steps

1. Send an HTTP GET request to the challenge endpoint.
2. Extract all headers starting with `X-Flag-`.
3. Sort them by their numeric index.
4. Concatenate their values.
5. Print the full flag.

## Solution

Running the exploit successfully reconstructs the hidden flag:

```
ITASEC{th3_1nt3rn3t_w0rk5_1n_my5t3r10us_w4ys}
```

## Key Takeaway

This challenge demonstrates how flags (or secrets) can be hidden in **HTTP headers**. Proper enumeration of all headers and ordering them correctly is essential to recover the full flag.
