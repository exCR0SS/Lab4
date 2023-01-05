# Напишите программу, в которой создается двумерный массив, который
# выводи прямоугольник из цифр 2;

class Main:

    height = int(input("Введите высоту: "))
    width = int(input("Введите ширину: "))
    # userSymbol = input("Введите символ, которым необходимо нарисовать прямоугольник: ")
    userSymbol = str(2)

    for i in range(height):
        if i == 0 or i == height-1:
            print(userSymbol * width)
        else:
            print(userSymbol, ' ' * (width - 2), userSymbol, sep='')