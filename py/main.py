"""Основной файл
ver 0.0.2
"""

collection = []

is_start = True

while is_start:
    print("\n1-Показать задачи")
    print("2-Добавить задачу")
    print("3-Изменить задачу")
    print("4-Удалить задачу")
    print("0-Выход")

    choice_user = input("Введите ваш выбор: ")

    if choice_user == "1":
        if len(collection) == 0:
            print("ЗАдач нет")
        else:
            print("\n⭣ Ваши задачи ⭣")
            for i in range(len(collection)):
                print(i + 1, "-", collection[i])
            print(" - Вот и все -")

    elif choice_user == "2":
        task = input("Введите название задачи: ")
        collection.append(task)
        print("Задача добавлена")

    elif choice_user == "3":
        if len(collection) == 0:
            print("Список задач пуст")
        else:
            for i in range(len(collection)):
                print(i + 1, "-", collection[i])

            number = int(input("Введите номер задачи: "))

            if number >= 1 and number <= len(collection):
                new_task = input("Введите новое название: ")
                collection[number - 1] = new_task
                print("Задача изменена")
            else:
                print("Такой задачи нет")

    elif choice_user == "4":
        if len(collection) == 0:
            print("Список задач пуст")
        else:
            for i in range(len(collection)):
                print(i + 1, "-", collection[i])

            number = int(input("Введите номер задачи: "))

            if number >= 1 and number <= len(collection):
                collection.pop(number - 1)
                print("Задача удалена")
            else:
                print("Такой здачи нет")

    elif choice_user == "0":
        print("Всё, конец")
        is_start = False

    else:
        print("Такого пункта нет")
