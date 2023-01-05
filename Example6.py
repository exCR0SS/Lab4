# Напишите программу, в которой создается и инициализируется
# двумерный числовой массив. Затем из этого массива удаляется строка и
# столбец (создается новый массив, в котором по сравнению с исходным
# удалена одна строка и один столбец). Индекс удаляемой строки и индекс
# удаляемого столбца определяется с помощью генератора случайных чисел.

import random
import copy

class Main:

        sizeArray1 = int(input("Количество столбцов: "))
        sizeArray2 = int(input("Количество строк: "))
        numArray = []
        rndDelRow = random.randint(0, (sizeArray2 - 1))
        rndDelColumn = random.randint(0, (sizeArray1 - 1))

        for i in range(sizeArray2):
            numArray.append([random.randint(1, 10) for n in range(sizeArray1)])

        newNumArray = copy.deepcopy(numArray)

        newNumArray.pop(rndDelRow)

        for i in range(sizeArray2 - 1):
            newNumArray[i].pop(rndDelColumn)

        print("Исходный массив: ", *numArray)
        print("Удалена строка с индексом: ", rndDelRow, "и столбец с индексом: ", rndDelColumn)
        print("Новый массив: ", *newNumArray)

