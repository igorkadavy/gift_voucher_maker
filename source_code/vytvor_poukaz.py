from PIL import Image, ImageDraw, ImageFont
import random
import subprocess

def get_promo_code(num_chars):
     code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     code = ''
     for _ in range(0, num_chars):
         slice_start = random.randint(0, len(code_chars) - 1)
         code += code_chars[slice_start: slice_start + 1]
     return code

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

image = Image.open("darkovy_poukaz_sablona.jpg")

draw = ImageDraw.Draw(image)

file_with_values = open("data.txt", "r")

price_font = ImageFont.truetype("Z:\\Igor Kadavý\\poukazy\\fonts\\TCM_____.TTF", 120)
price_value_tmp = file_with_values.readline()
price_value = "".join([price_value_tmp[i] for i in range(len(price_value_tmp) - 1)])
price_text = str(price_value) + " Kč"
price_position = (1650, 270)

code_font = ImageFont.truetype("Z:\\Igor Kadavý\\poukazy\\fonts\\TCM_____.TTF", 70)
code_text = get_promo_code(10)
copy2clip(code_text)
code_position = (1650, 485)

date_font = ImageFont.truetype("Z:\\Igor Kadavý\\poukazy\\fonts\\TCM_____.TTF", 50)
date_text_tmp = file_with_values.readline()
date_text = "".join([date_text_tmp[i] for i in range(len(date_text_tmp) - 1)]) if date_text_tmp[-1] == "\n" else date_text_tmp
date_position = (1650, 650)

draw.text(price_position, price_text, font=price_font, fill=(0, 0, 0, 1))
draw.text(code_position, code_text, font=code_font, fill=(255, 255, 255, 1))
draw.text(date_position, date_text, font=date_font, fill=(0, 0, 0, 1))

image.save(price_value + "_slevovy_kupon_" + code_text + ".pdf")
