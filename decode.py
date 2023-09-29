from PIL import Image
from re import findall

def stega_decrypt():
    a = []
    keys = []           #сюда будем записывать сообщение
    img = Image.open(input("path to image: "))
    pix = img.load()
    f = open(input('path to keys: '),'r')
    y = str([line.strip() for line in f])           #убираем пробелы из каждой строки

    for i in range(len(findall(r'\((\d+)\,', y))):
        keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))         #записываем координаты пикселей из файла с ключами
    for key in keys:
        a.append(pix[tuple(key)][0])                #берем значение красного выбранных элементов
    return ''.join([chr(elem) for elem in a])

print("you message: ", stega_decrypt())
