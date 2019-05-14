import os
import sys
from textwrap import fill
from PIL import Image, ImageDraw, ImageFont

i = 1  # Iteration start


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


while True:
    # Main Menu
    
    while True:
        print('Which language would you like to translate to?')
        try:
            q1 = int(input('1. Davek\n2. Iokharic\n3. Rellanic\n9. Exit\n'))
            if q1 == 1:
                lang = 'Davek'
                font = ImageFont.truetype(resource_path('Davek.otf'), 28, encoding='unic')
                fcolor = 'silver'
                real_text_width = 625
                break
            elif q1 == 2:
                lang = 'Iokharic'
                font = ImageFont.truetype(resource_path('Iokharic.otf'), 28, encoding='unic')
                fcolor = 'red'
                real_text_width = 640
                break
            elif q1 == 3:
                lang = 'Rellanic'
                font = ImageFont.truetype(resource_path('Rellanic.otf'), 28, encoding='unic')
                fcolor = 'darkgreen'
                real_text_width = 645
                break
            elif q1 == 9:
                exit(666)
            else:
                print('Please enter a valid response')
        except ValueError:
            print('Please enter a valid response(Use numbers to select)')

    # Enter English Here
    
    print(f'{lang} chosen')
    string = input('Enter English\n')
    titlestring = string.replace('?', '_')  # Get rid of ?'s as they break the script on most machines
    newstring = string.replace(',', ' ')  # Get rid of ,'s as they are'nt in the font yet
    fill_string = fill(newstring, 50)  # Fill string to make paragraph style text
    text_width, text_height = font.getsize(string)
    
    # My quick attempt at a dynamic box around the filled text. Not sure how to do it better yet. Will probably come back to this one day
    
    count = 0
    for count in range(len(string[::50])):
        count += 2
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
        real_text_width = text_width + 10
    else:
        real_text_height = text_height + 10
        real_text_width = text_width + 10

    # Make the image here
    
    canvas = Image.new('RGB', (real_text_width, real_text_height), 'black')
    draw = ImageDraw.Draw(canvas)
    draw.text((5, 5), fill_string, fcolor, font)
    
    # Save the image with brief reference along with a copy to directly send to someone in the session
    
    canvas.save(f'{i}. {lang}' + '.png', "PNG")
    canvas.save(f'{i}. {lang} - ' + titlestring[:15] + '.png', "PNG")
    i += 1  # Iteration plus 1 to keep the files organized for the user
