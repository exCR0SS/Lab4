# Напишите программу «Шифр Цезаря», которая зашифровывает
# введенный текст. Используете кодовую таблицу символов. При запуске программы в консоль необходимо вывести сообщение: «Введите текст для
# шифрования», после ввода текста, появляется сообщение: «Введите ключ». После того как введены все данные, необходимо вывести преобразованную
# строку с сообщением «Текст после преобразования : ». Далее необходимо задать вопрос пользователю: «Выполнить обратное преобразование? (y/n)»,
# если пользователь вводит «y», тогда выполнить обратное преобразование. Если пользователь вводит «n», того программа выводит сообщение «До
# свидания!». Если пользователь вводит что-то другое, отличное от «y» или «n», то программа ему выводит сообщение: «Введите корректный ответ».


class Main:

    userText = str(input("Введите слово для шифрования: ").lower())
    userKey = int(input("Введите ключ: "))


    def get_encrypt(txt, key, encrypt):
        # Функция шифровки / дешифровки в зависимости от 3-го параметра, True - шифрует, False - дешифрует.
        alphabetEN = 'abcdefghijklmnopqrstuvwxyz'
        alphabetRU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        resText = ''

        if alphabetRU.find(txt[0]) != -1:
            for i in range(len(txt)):
                if alphabetRU.index(txt[i]) + abs(key) <= len(alphabetRU) - 1:
                    resText += alphabetRU[alphabetRU.index(txt[i]) + (abs(key) if encrypt == True else -abs(key))]
                # elif alphabetRU.index(txt[i]) + abs(key) > len(alphabetRU) - 1:
                else:
                    resText += alphabetRU[alphabetRU.index(txt[i]) + (abs(key) if encrypt == True else -abs(key)) - len(alphabetRU)]
        else:
            for i in range(len(txt)):
                if alphabetEN.index(txt[i]) + abs(key) <= len(alphabetEN) - 1:
                    resText += alphabetEN[alphabetEN.index(txt[i]) + (abs(key) if encrypt == True else -abs(key))]
                # elif alphabetEN.index(txt[i]) + abs(key) > len(alphabetEN) - 1:
                else:
                    resText += alphabetEN[alphabetEN.index(txt[i]) + (abs(key) if encrypt == True else -abs(key)) - len(alphabetEN)]
        return resText


    print(get_encrypt(userText, userKey, True))

    while True:
        decisionUser = str(input("Выполнить обратное преобразование? (y/n) ").lower())
        if decisionUser == 'y':
            print(get_encrypt(get_encrypt(userText, userKey, True), userKey, False))
            break
        elif decisionUser == 'n':
            break
        else:
            print("Введите корректный ответ.")
            continue