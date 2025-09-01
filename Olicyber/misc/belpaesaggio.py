from PIL import Image

with Image.open("belpaesaggio.gif") as gif:
    print(f"Formato: {gif.format}")
    print(f"Dimensione: {gif.size}")
    print(f"Informazioni: {gif.info}")

if "comment" in gif.info:
    print(f"Commenti: {gif.info["comment"]}")
else:
    print("Nessun commento trovato")


"""import numpy as np
from PIL import Image

img = Image.open("belpaesaggio.gif")
data = np.array(img)

print(data)
"""