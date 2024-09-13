from PIL import Image, ImageDraw, ImageFont, ImageOps

border_width = 5
font = ImageFont.truetype("Arial.ttf", 40)

for i in range(3):
    image = Image.new("RGB", (100 - 2*border_width, 100 - 2*border_width))
    image = ImageOps.expand(image, border_width, fill= "blue")
    draw = ImageDraw.Draw(image)
    draw.text((50, 50), str(i+1), font = font, fill = "red", anchor= "mm")
    
    image.save(f"out{i+1}.png")
    image.show()
