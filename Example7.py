# Напишите программу, в которой создается двумерный числовой массив
# и этот массив заполняется «змейкой»: сначала первая строка (слева направо),
# затем последний столбец (снизу вверх), вторая строка (слева направо) и так далее.

class Main:

    numArray = []
    m, j = 0, 0
    num = 1

    for i in range(5):
        numArray.append([])
        for n in range(5):
            if j in range(4):
                numArray[m].append(num)
            num += 1
        m += 1

    print(*numArray)
