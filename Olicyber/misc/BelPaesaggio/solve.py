from PIL import Image

num_key_frames = 8

with Image.open('./belpaesaggio.gif') as im:
    for i in range(num_key_frames):
        if i == 3:
            im.seek(im.n_frames // num_key_frames * i)
            im.save('{}.png'.format(i))
        else:
            pass
