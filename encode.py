from PIL import Image, ImageDraw
from random import randint

def stega_encrypt():
    keys = []
    img = Image.open(input("path to image: "))
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()                #передаем картинку
    f = open('keys.txt', 'w')

    for elem in ([ord(elem) for elem in input("text here: ")]):
        key = (randint(1, width-10), randint(1, height-10))     #выбираем случайный пиксель
        g, b = pix[key][1:]                                     #берем значения синего и зеленого
        draw.point(key, (elem, g, b))                           #передаем координаты и цвет
        f.write(str(key)+'\n')

    print('keys were written to the keys.txt file')
    img.save("newimage.png", "PNG")                             #сохраняем изображение
    f.close()

stega_encrypt()