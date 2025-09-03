# Floppy Bird – Writeup

## Challenge Description
```
I have recreated one of the most classic games in the browser, can you score 1000 points and get the flag?

Website: http://floppybird.challs.olicyber.it
```
In this challenge, the flag is awarded after reaching a certain score in the game. Instead of playing manually, we can exploit the server’s API to submit arbitrary scores until the flag is revealed.

## Exploit
```python
import requests, json

site = "http://floppybird.challs.olicyber.it/"
token = json.loads(requests.get(site + "get-token").text)["token"]
r = ""

for i in range(1001):
    r = requests.post(site + "update-score", json={"token": token, "score": i}).json()
    if "flag" in r:
        print(r["flag"])
        break
````

## Code Analysis

1. **Token Retrieval**

   * A unique token is obtained from `/get-token`.
   * This token is required for all score submissions.

2. **Score Submission**

   * A loop tests scores from `0` up to `1000`.
   * Each score is submitted via POST to `/update-score` with:

     ```json
     {
       "token": "<your_token>",
       "score": <i>
     }
     ```

3. **Flag Detection**

   * When we reach 1000 points we win so on the 1000th request we retrieve the flag from the JSON response and stop the script.
## Exploitation Steps

1. Request a valid token from the challenge server.
2. Submit increasing scores to `/update-score`.
3. Check the server’s response for the `"flag"` field.
4. Stop when the flag is received and print it.

## Solution

Running the exploit successfully retrieves the flag from the server’s response:

```
ptm{n3v3r_7rus7_cl13n7_s1d3_d4ta}
```

## Key Takeaway

This challenge highlights **broken game logic and lack of server-side validation**.
The server trusts user-submitted scores without verifying their authenticity, making it trivial to cheat and obtain the flag. Secure systems must validate results server-side instead of relying on client input.
