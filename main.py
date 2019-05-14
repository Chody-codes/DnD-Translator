from PIL import Image, ImageDraw, ImageFont
from textwrap import fill
import os
import sys

i = 1


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


while True:
    lang = 'ERROR'
    font = ImageFont.truetype("arial.ttf", 15)
    fcolor = 'white'
    for main in range(100):
        print('Which language would you like to translate to?')
        try:
            q1 = int(input('1. Davek\n2. Iokharic\n3. Rellanic\n9. Exit\n'))
            if q1 == 1:
                text_length = 650
                lang = 'Davek'
                font = ImageFont.truetype(resource_path('Davek.otf'), 28, encoding='unic')
                fcolor = 'silver'
                break
            elif q1 == 2:
                # iokharic()
                text_length = 650
                lang = 'Iokharic'
                font = ImageFont.truetype(resource_path('Iokharic.otf'), 28, encoding='unic')
                fcolor = 'red'
                break
            elif q1 == 3:
                text_length = 650
                lang = 'Rellanic'
                font = ImageFont.truetype(resource_path('Rellanic.otf'), 28, encoding='unic')
                fcolor = 'darkgreen'
                break
            elif q1 == 9:
                exit(666)
            else:
                print('Please enter a valid response')
        except ValueError:
            print('Please enter a valid response(Use numbers to select)')
    print(f'{lang} chosen')
    string = input('Enter English\n')
    titlestring = string.replace('?', '_')
    newstring = string.replace(',', ' ')
    fill_string = fill(newstring, 50)

    text_width, text_height = font.getsize(string)
    count = 0
    for count in range(len(string[::50])):
        count += 2
    # print(count)
    if len(string) > 150:
        real_text_height = len(string) * count // 6
    elif len(string) > 125:
        real_text_height = len(string) * count // 5
    elif len(string) > 100:
        real_text_height = len(string) * count // 4
    elif len(string) > 75:
        real_text_height = len(string) * count // 3
    elif len(string) > 50:
        real_text_height = len(string) * count // 2
    elif len(string) > 25:
        real_text_height = len(string) * count // 1
    else:
        real_text_height = text_height + 10
    canvas = Image.new('RGB', (text_length, real_text_height), 'black')
    draw = ImageDraw.Draw(canvas)
    draw.text((5, 5), fill_string, fcolor, font)

    canvas.save(f'{i}. {lang}' + '.png', "PNG")
    canvas.save(f'{i}. {lang} -' + titlestring[:15] + '.png', "PNG")
    i += 1
    # canvas.show()
