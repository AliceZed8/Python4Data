from argparse import ArgumentParser
from pathlib import Path
import os.path


parser = ArgumentParser()
parser.add_argument("-d", "--dirpath", default = ".")
parser.add_argument("-f", "--files", nargs = "+")
args = parser.parse_args()


path = Path(args.dirpath)
filenameList = args.files


#если имена файлов отсутствуют
if (filenameList == None):
    filesCount = 0
    filesSize = 0
    for entry in path.iterdir():
        if (entry.is_file()):
            filesCount += 1
            filesSize  += entry.stat().st_size

    print(f"Files count: {filesCount} ({filesSize} Bytes)")
    exit()


#открываем файлы и записываем
with open(path.joinpath("exists.txt"), "w+") as file1, open(path.joinpath("not_exists.txt"), "w+") as file2:
    for filename in filenameList:
        if (os.path.exists(path.joinpath(filename))):
            print(filename, "exists")
            file1.write(filename + "\n")

        else:
            print(filename, "not exists")
            file2.write(filename + "\n")





