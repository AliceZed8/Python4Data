from argparse import ArgumentParser
from PIL import Image
from skimage.exposure import histogram as SKHistogram
from skimage import io

from matplotlib import pyplot as plt
from matplotlib import use as MPLUseBackend
MPLUseBackend("gtk4agg")



parser = ArgumentParser()
parser.add_argument("-p", "--path")
args = parser.parse_args()
path = args.path

if (path == None): exit()



#Используем PIL
histogram = []
image = None
with Image.open(path) as img:
    img = img.convert("RGB")
    image = img.copy()
    histogram = img.histogram()
        

r_channel = histogram[0:256]
g_channel = histogram[256:512]
b_channel = histogram[512:768]


rgb = [r_channel[i] + g_channel[i] + b_channel[i] for i in range(256)]
plt.subplot2grid((4,2), (0,0), colspan= 1, rowspan= 4)
plt.imshow(image)
plt.axis("off")
plt.title("Image")


# Гистограмма изображения
plt.subplot2grid((4, 2), (0, 1))
#plt.bar(range(256), rgb, fill = True, color = "gray") #другой способ вывода
plt.stairs(rgb, fill = True, color = "gray")
plt.title("Image histogram")


#Используем Skimage
img = io.imread(path)
#plt.hist(img.ravel(), bins=256, fill = True, color = "gray") #другой способ вывода

plt.subplot2grid((4, 2), (1, 1))
plt.hist(img[:, :, 0].ravel(), bins= 256, fill = True, color = "red")
plt.title("Channel R histogram")

plt.subplot2grid((4, 2), (2, 1))
plt.hist(img[:, :, 1].ravel(), bins= 256, fill = True, color = "green")
plt.title("Channel G histogram")

plt.subplot2grid((4, 2), (3, 1))
plt.hist(img[:, :, 2].ravel(), bins= 256, fill = True, color = "blue")
plt.title("Channel B histogram")
    
        

plt.tight_layout()
plt.show()

    

    








