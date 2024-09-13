from PIL import Image, ImageFont, ImageDraw

#размер водяного знака
wt_size = 100

with Image.open("RGB.jpg") as img:
    wtmark = Image.open("wtmark.png")
    wtmark.thumbnail((wt_size, wt_size))
    w, h = img.size
    

    wtmark.putalpha(130)
    wt_mask = wtmark.convert("L").point(lambda x: min(x, 150)) #маска
    
    
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Arial.ttf", 14)

    for i in range(0, int(w/wt_size), 2):
        for j in range(0, int(h/wt_size), 2):
            #вставляем водяной знак с маской, и текст
            img.paste(wtmark, (i*wt_size, j*wt_size), mask = wt_mask)
            draw.text((wt_size*i+50 , wt_size*j + 50), "CHEESE", font = font, fill = (255, 255, 0, 130), anchor= "mm")
    img.save("out.jpg")
    img.show()
