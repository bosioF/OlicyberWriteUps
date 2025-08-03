import requests, json

site = "http://floppybird.challs.olicyber.it/"
token = json.loads(requests.get(site + "get-token").text)["token"]
r = ""

for i in range(1001):
    r = requests.post(site + "update-score", json={"token": token, "score": i}).text
    print(i)