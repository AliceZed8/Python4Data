from argparse import ArgumentParser
from pathlib import Path
import shutil
import os.path


parser = ArgumentParser()
parser.add_argument("-id", "--indir", default = ".") #папка в которой находятся файлы exists.txt и not_exists.txt
parser.add_argument("-od", "--outdir", default = ".")

args = parser.parse_args()
inPath = Path(args.indir)
outPath = Path(args.outdir)


try:
    with open(inPath.joinpath("not_exists.txt")) as f:
        lines = f.readlines()
        for line in lines:
            outPath.joinpath(line).touch()
except FileNotFoundError as e:
    print(e.strerror)

