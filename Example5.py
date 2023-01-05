# Напишите программу, в которой создается двумерный целочисленный массив. Он заполняется случайными числами. Затем в этом массиве строи и
# столбцы меняются местами: первая строка становится первым столбцом, вторая строка становиться вторым столбцом и так далее. Например, если
# исходный массив состоял из 3 строк и 5 столбцов, то в итоге получаем массив из 5 строк и 3 столбцов.

# Применена библиотека NumPy, нет среди стандартных библиотек. Установка через CMD: ...\Python\Scripts\pip install "numpy"
import random
import numpy

class Main:

    sizeArray1 = int(input("Количество столбцов: "))
    sizeArray2 = int(input("Количество строк: "))
    numArray = []


    for i in range(sizeArray2):
        numArray.append([random.randint(1, 10) for n in range(sizeArray1)])

    newArray = numpy.transpose(numArray)

    print("Исходный массив: ", *numArray)
    print("Транспонированный массив: ", *newArray)

