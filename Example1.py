# Напишите программу, которая выводить в консольное окно
# прямоугольник, размеры сторон которого, ширина: 23 колонки, высота: 11 строк;

class Main:

    height = int(input("Введите высоту: "))
    width = int(input("Введите ширину: "))
    userSymbol = input("Введите символ, которым необходимо нарисовать прямоугольник: ")

    for i in range(height):
        if i == 0 or i == height-1:
            print(userSymbol * width)
        else:
            print(userSymbol, ' ' * (width - 2), userSymbol, sep='')