import hashlib
import random
from PIL import Image, ImageDraw, ImageFont

def generate_nft():
    seed = random.randint(0, 1000000)
    random.seed(seed)
    hash = hashlib.sha256(str(seed).encode()).hexdigest()
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)]
    im = Image.new('RGB', (512, 512), colors[0])
    pattern_size = 32
    draw = ImageDraw.Draw(im)
    for x in range(0, 512, pattern_size):
        for y in range(0, 512, pattern_size):
            pattern_type = random.randint(0, 2)
            if pattern_type == 0:
                draw.rectangle((x, y, x+pattern_size, y+pattern_size), fill=colors[random.randint(1, len(colors)-1)])
            elif pattern_type == 1:
                draw.ellipse((x, y, x+pattern_size, y+pattern_size), fill=colors[random.randint(1, len(colors)-1)])
            else:
                draw.polygon([(x, y), (x+pattern_size/2, y+pattern_size), (x+pattern_size, y)], fill=colors[random.randint(1, len(colors)-1)])
    font = ImageFont.truetype('arial.ttf', 24)
    text = hash[:32] + '\n' + hash[32:64] + '\n' + hash[64:]
    text_width, text_height = draw.textsize(text, font)
    max_width = 512
    max_height = 512
    if text_width > max_width or text_height > max_height:
        font_size = 24
        while draw.textsize(text, ImageFont.truetype('arial.ttf', font_size))[0] > max_width or draw.textsize(text, ImageFont.truetype('arial.ttf', font_size))[1] > max_height:
            font_size -= 1
        font = ImageFont.truetype('arial.ttf', font_size)
    text_width, text_height = draw.textsize(text, font)
    text_x = (512 - text_width) / 2
    text_y = (512 - text_height) / 2
    r, g, b = im.convert('RGB').getpixel((0, 0))
    avg_color = (r + g + b) // 3
    if avg_color < 128:
        text_color = (255, 255, 255)
    else:
        text_color = (0, 0, 0)
    draw.multiline_text((text_x, text_y), text, font=font, fill=text_color, align='center')
    return [im, hash]