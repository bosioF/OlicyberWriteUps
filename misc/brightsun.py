
#si risolve abbassando la luminosita con gimp
from PIL import Image

with Image.open("Bright Sun.png") as image:
    print(f"Formato: {image.format}")
    print(f"Dimensione: {image.size}")
    print(f"Informazioni: {image.info}")

if "comment" in image.info:
    print(f"Commenti: {image.info["comment"]}")
else:
    print("Nessun commento trovato")


"""import numpy as np
from PIL import Image

img = Image.open("belpaesaggio.image")
data = np.array(img)

print(data)
"""