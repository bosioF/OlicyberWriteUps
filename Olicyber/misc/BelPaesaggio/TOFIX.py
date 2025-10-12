from PIL import Image
from PIL import GifImagePlugin

imageObject = Image.open("belpaesaggio.gif")

if imageObject.is_animated:
    for frame in range(imageObject.n_frames):
        imageObject.seek(frame)
        imageObject.show()


# da fixare, comunque basta estrarre i frame dalla GIF e nel quarto troviamo la flag
