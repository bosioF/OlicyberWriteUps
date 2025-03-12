"""
import base64
import pickle
import requests

# Creare una classe che replica HeaderFilterGadget in Python
class HeaderFilterGadget:
    def __init__(self, header):
        self.header = header

    def set(self):
        # Modificare l'intestazione in base al tipo
        if self.header == "FLAG":
            self.flag = "FLAG{esempio_flag}"  # Flag da ottenere
        elif self.header == "Location":
            self.location = "https://afeverdream.challs.olicyber.it/"  # Aggiungere una location per testing

    def get(self):
        if self.header == "FLAG":
            return self.flag
        elif self.header == "Location":
            return self.location

# Creare il payload
gadget = HeaderFilterGadget("FLAG")
gadget.set()

# Serializzare l'oggetto
serialized = pickle.dumps(gadget)

# Codificare in Base64
payload = base64.b64encode(serialized).decode()

print("Payload generato:")
print(payload)
"""
import requests


url = "https://afeverdream.challs.olicyber.it/index.php"

#response = requests.post(url, data={"payload": payload})

data = {"payload": ""}
response = requests.post(url, data=data)

print("Risposta del server:")
print(response.text)