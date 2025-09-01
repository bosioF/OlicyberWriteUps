# SVG Comment Challenge – Writeup

## Challenge Description
The challenge provides an `.svg` file. The flag is not visible in the image itself but is hidden inside the file contents. By inspecting the file, we can find a comment that contains the flag.

## Exploit
```python
import requests
import re

url = 'http://vectorcraft.challs.olicyber.it/logo.svg'
r = requests.get(url)
flag = re.findall(r'<!--(.*?)-->', r.text, re.DOTALL)
print(flag[0])
````

## Code Analysis

1. **Target File**
   The exploit downloads the `.svg` file using an HTTP GET request.

2. **Comment Extraction**

   * SVG files often contain XML comments.
   * The regex `<!--(.*?)-->` is used to match anything between `<!--` and `-->`.
   * The `re.DOTALL` flag ensures that multiline comments are matched.

3. **Retrieving the Flag**

   * `re.findall()` returns a list of all comments found in the file.
   * The script prints the first comment (`flag[0]`), which contains the flag.

## Exploitation Steps

1. Download the `.svg` file from the provided URL.
2. Search for comments inside the file.
3. Extract the content of the comment.
4. Print the result.

## Solution

Running the exploit prints the hidden flag:

```
ITASEC{y0u_c4n_f1nd_t3xt_wh3r3_y0u_l3ast_3xp3ct_1t}
```

## Key Takeaway

This challenge shows how flags can be hidden in **file metadata or comments**, not necessarily in the visible output. Always inspect the source when working with web or file-based challenges.
