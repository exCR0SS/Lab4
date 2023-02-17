# Напишите программу, в которой создается двумерный массив, который
# выводит прямоугольный треугольник;


height = int(input("Введите высоту: "))
width = int(input("Введите ширину: "))
userSymbol = input("Введите символ, которым необходимо нарисовать треугольник: ")

for i in range(height):
    if i == 0:
        print(userSymbol)
    elif i == height - 1:
        print(userSymbol * (width + 1))
    else:
        print(userSymbol, ' ' * (width - (width - i)), userSymbol, sep='')
