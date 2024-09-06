from pathlib import Path
from argparse import ArgumentParser
import shutil


parser = ArgumentParser()
parser.add_argument("-p", "--path", default = ".")
args = parser.parse_args()

path = Path(args.path)


#список файлов
pathList = [entry for entry in path.iterdir() if (entry.is_file() and (entry.stat().st_size < 2048))]

if (pathList == []):
    print("Empty")
    exit()


#создаем папку
newPath = path.joinpath("small")
newPath.mkdir(exist_ok= True)

#выводим список файлов и копируем
for entry in pathList:
    print(entry.name)
    shutil.copy(entry, newPath.joinpath(entry.name))



