from argparse import ArgumentParser
from PIL import Image


parser = ArgumentParser()
parser.add_argument("-p", "--path")
args = parser.parse_args()
path = args.path

if (path == None): exit()


with Image.open(path) as img:
    img.load()
    pixels = list(img.getdata())

    rc, gc, bc = 0, 0, 0
    
    for pixel in pixels:
        r, g, b = pixel
        rc += r
        gc += g
        bc += b
    maxV = max(rc, gc, bc)
    
    img.show()
    if (maxV == rc): print("Red")
    elif (maxV == gc): print("Green")
    else: print("Blue")
    



