import requests

url = "https://easyshop.challs.olicyber.it/send"

data = {
    "to": "64b21c49485884f04597d7250a389bdb2b0ca548c0f212f8c22bc3c5546d7437",
    "amount": "1000"
}

response = requests.post(url, data=data)

print(f"Status Code: {response.status_code}")
print(f"Risposta: {response.text}")
