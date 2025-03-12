import re

def estrai_flag(path):
    try:    
        with open(path, 'rb') as file:
            bytes_data = file.read()
            matches = re.findall(rb'flag\{.*?\}', bytes_data)
            if matches:
                for match in matches:
                    print(match.decode('utf-8', errors='ignore'))
            else:
                print("Nessun flag trovato")
    except FileNotFoundError:
        print("File non trovato")

estrai_flag("/home/bosio/Downloads/flag.png")


"""import numpy as np
from PIL import Image

with Image.open("/home/bosio/Downloads/flag.png") as png:
    print(f"Formato: {png.format}")
    print(f"Dimensione: {png.size}")
    print(f"Informazioni: {png.info}")

if "comment" in png.info:
    print(f"Commenti: {png.info["comment"]}")
else:
    print("Nessun commento trovato")

img = Image.open("/home/bosio/Downloads/flag.png")
data = np.array(img)

print(data)

from PIL import Image

img = Image.open("belpaesaggio.gif")
data = np.array(img)

print(data)
"""