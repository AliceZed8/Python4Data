from PIL import Image
from argparse import ArgumentParser
from pathlib import Path
import numpy as np


from skimage.transform import warp, AffineTransform
from skimage.exposure import equalize_adapthist, equalize_hist, rescale_intensity, adjust_gamma, adjust_log, adjust_sigmoid
from skimage.filters import gaussian
from skimage.util import random_noise
import pylab as pl
import random


def randRange(a, b):
    #random float in range
    return pl.rand() * (b - a) + a

    

#Аффинное преобразование
def _affineTransform(img):
    tform = AffineTransform(scale=(randRange(0.5, 1.5), randRange(0.5, 1.5)),
                            rotation=randRange(-0.2, 0.2),
                            shear=randRange(-0.2, 0.2),
                            translation=(randRange(-img.shape[0]//10, img.shape[0]//10),
                                         randRange(-img.shape[1]//10, img.shape[1]//10)))
    return warp(img, tform.inverse, mode='reflect')    

#Вырезка
def _crop(img):
    margin = 1/10
    start = [int(randRange(0, img.shape[0] * margin)),
             int(randRange(0, img.shape[1] * margin))]
    end = [int(randRange(img.shape[0] * (1-margin), img.shape[0])), 
           int(randRange(img.shape[1] * (1-margin), img.shape[1]))]
    return img[start[0]:end[0], start[1]:end[1]]


#изменение яркости
def _intensity(img):
    return rescale_intensity(img,
                             in_range=tuple(pl.percentile(img, (randRange(0,10), randRange(90,100)))),
                             out_range=tuple(pl.percentile(img, (randRange(0,10), randRange(90,100))))).astype(np.uint8)
#доавление шума
def _noise(img):
    var = randRange(0.001, 0.01)
    return random_noise(img, var=var)

#гауссов фильтр
def _gaussian(img):
    return gaussian(img, sigma=randRange(0, 5))

#Адаптивная коррекция гистограммы
def _equalizeAdapthist(img):
    return equalize_adapthist(img)

#Коррекция гистограммы
def _equalizeHist(img):
    return equalize_hist(img)

#Гамма коррекция
def _adjustGamma(img):
    return adjust_gamma(img, gamma=randRange(0.5, 1.5))

#Логарифмическая коррекция
def _adjustLog(img):
    return adjust_log(img)

#Сигмовидная коррекция
def _adjustSigmoid(img):
    return adjust_sigmoid(img)


parser = ArgumentParser()
parser.add_argument("-p", "--path")
parser.add_argument("--affineTransform",          action= "store_true", help = "Геометрическое преобразование")
parser.add_argument("--crop",               action= "store_true", help = "Вырезка")
parser.add_argument("--intensity",          action= "store_true", help = "Изменение яркости")
parser.add_argument("--noise",              action= "store_true", help = "Добавление шума")
parser.add_argument("--gaussian",           action= "store_true", help = "Фильтр Гаусса")
parser.add_argument("--equalizeAdapthist",          action= "store_true", help = "Адаптивная коррекция гистограммы")
parser.add_argument("--equalizeHist",               action= "store_true", help = "Коррекция гистограммы")
parser.add_argument("--adjustGamma",              action= "store_true", help = "Гамма коррекция")
parser.add_argument("--adjustLog",                action= "store_true", help = "Логарифмическая коррекция")
parser.add_argument("--adjustSigmoid",            action= "store_true", help = "Сигмовидная коррекция")
parser.add_argument("--complex",            action= "store_true", help = "Комплексное преобразование")



args = parser.parse_args()
path = args.path
if (path == None): exit()


# Список преобразований
transformsList = [
    _affineTransform,
    _crop,
    _intensity,
    _noise,
    _gaussian,
    _equalizeAdapthist,
    _equalizeHist,
    _adjustGamma,
    _adjustLog,
    _adjustSigmoid,
]

# Выбранные преобразования
selectedList = []
for trans in transformsList:
    if getattr(args, trans.__name__.lstrip("_")):
        selectedList.append(trans)

# Если ничего не выбрано
if (len(selectedList)== 0): exit()


files = sorted(Path(path).glob("*.jpg"))
fileNum = len(files) #номер сохраняемого файла


for file in files:
    print("# Augment", path + file.name)
    img = pl.imread(path + file.name)
    
    # Если указан аргумент complex, применяем все указанные преобразования
    if args.complex:
        for filt in selectedList:
            img = filt(img)
        
        # сохраняем
        imgPath = "0"*(4 - len(str(fileNum))) + str(fileNum) + ".jpg"
        pl.imsave(path + imgPath, img)

        print("New image", imgPath)
        fileNum += 1
        continue
            
    for filt in selectedList:
        imgTemp = filt(img.copy())
        
        # сохраняем
        imgPath = "0"*(4 - len(str(fileNum))) + str(fileNum) + ".jpg"
        pl.imsave(path + imgPath, imgTemp)

        print("New image", filt.__name__, imgPath)
        fileNum += 1
    
    






























