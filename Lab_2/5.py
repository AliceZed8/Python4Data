from PIL import Image
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()
parser.add_argument("-ft", "--ftype")
args = parser.parse_args()
ftype = args.ftype

if (ftype == None): exit()


files = Path(".").glob(f"*{ftype}")
for file in files:
    image = Image.open(file.name)
    image.thumbnail((50,50))
    image.show()

