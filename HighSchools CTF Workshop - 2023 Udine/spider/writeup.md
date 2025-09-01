# Web Spidering Challenge – Writeup

## Challenge Description
We are tasked with retrieving a flag that is split across two different files hosted on a challenge server. The files are hidden inside different folders, and the goal is to combine their contents to reconstruct the complete flag.

## Exploit
```python
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
    print(full_flag)
else:
    print("error")
````

## Code Analysis

1. **Libraries**
   The script uses the `requests` library to send HTTP GET requests.

2. **Target URLs**
   Two URLs are provided:

   * `url1` points to `flag1.txt` inside `supe3s3cretf0lder`.
   * `url2` points to `flag2.txt` inside `standardNonSecretFolder`.

3. **Fetching Function**
   The `fetch_flag_part` function:

   * Sends a GET request to the given URL.
   * Returns the response text with whitespace removed using `.strip()`.

4. **Flag Reconstruction**

   * The script downloads both parts of the flag.
   * `part1_cleaned = part1.split('\n')[0]` ensures only the first line of `flag1.txt` is used (in case of extra whitespace/newlines).
   * Concatenates `part1_cleaned + part2` to rebuild the full flag.

5. **Output**
   If both parts are successfully retrieved, the complete flag is printed. Otherwise, it prints `"error"`.

## Exploitation Steps

1. Access the hidden folders on the challenge server.
2. Retrieve both `flag1.txt` and `flag2.txt`.
3. Clean and concatenate them.
4. Print the resulting flag.

## Solution

Running the script successfully fetches the two parts of the flag and reconstructs the final result:

```
flag{s3mbr1_un0_sp1d3R}
```

## Key Takeaway

This challenge tests **basic web enumeration and file retrieval**. By exploring non-standard folders and combining information, we reconstruct the hidden flag.
