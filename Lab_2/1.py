from PIL import Image

path = "bird.jpg"

with Image.open(path) as img:
    img.load()
    print(img.getbands())
    red, green, blue = img.split()
    
    zero_band = red.point(lambda _: 0)
    red_merge = Image.merge("RGB", (red, zero_band, zero_band))
    green_merge = Image.merge("RGB", (zero_band, green, zero_band))
    blue_merge =  Image.merge("RGB", (zero_band, zero_band,blue ))
    
    blue_merge.show()
    green_merge.show()
    red_merge.show()

    img.show()
