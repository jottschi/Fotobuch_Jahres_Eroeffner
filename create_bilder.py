#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
def center(output_path,text_to_draw):
    width, height = (400, 250)
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)
    my_font = ImageFont.truetype("bahnschrift.ttf", size=100)
    my_font.set_variation_by_name('SemiCondensed')
    font_width, font_height = my_font.getsize(text_to_draw)
    new_width = (width - font_width) / 2
    new_height = (height - font_height) / 2
    draw.text((new_width, new_height), text_to_draw, fill="white", font=my_font)
    image.save(output_path)

if __name__ == "__main__":
    
  for jahr in range(2003,2022):
    
    image_name= str(jahr) + "-01-01_01-00_001.jpg"
    print("Dateiname: " + image_name)
    center(image_name, str(jahr))
