"""Основной файл
ver 0.0.2
"""

is_running = True
collection = []

def show_collection(collection):
    print("=" * 30)

    if not collection:
        print("Список задач пуст")
    else:
        for i, task in enumerate(collection):
            print(f"{i + 1}. {task}")

    print("=" * 30)

while is_running:
    print(
        "\n1 - посмотреть задачи\n"
        "2 - добавить задачу\n"
        "3 - редактировать задачу\n"
        "4 - удалить задачу\n"
        "5 - выход"
    )
    clause_user = input("Введите свой выбор: ")
    match clause_user:
        case '1':
            show_collection(collection)
        case '2':
            task_name = input("Введите название задачи: ")
            if task_name.startswith(' '):
                if len(task_name) < 2:
                    print("Название не могет быть пустым")
                    continue
                else:
                    collection.append(f"задача {len(collection)}")
            else:
                collection.append(task_name)
        case '3':
            show_collection(collection)
            if not collection:
                continue
            select_edit = input("Введите номер задачи: ")
            if select_edit.isdigit():
                select_edit = int(select_edit)
                if 1 <= select_edit <= len(collection):
                    edit_name = input("Новое имя задачи: ")
                    if edit_name.strip():
                        collection[select_edit - 1] = edit_name
                        print(
                            f"Задача №{select_edit} "
                            f"успешно отредактирована!"
                        )
                    else:
                        print("Название задачи не может быть пустым")
                else:
                    print("Задачи с таким номером нет")
            else:
                print("Нужно ввести номер, а не букву")
        case '4':
            show_collection(collection)
            if not collection:
                continue
            delete_edit = input("Введите номер задачи для удаления: ")
            if delete_edit.isdigit():
                delete_edit = int(delete_edit)
                if 1 <= delete_edit <= len(collection):
                    deleted_task = collection.pop(delete_edit - 1)
                    print(
                        f"Задача '{deleted_task}' "
                        f"успешно удалена!"
                    )
                else:
                    print("Задачи с таким номером нет")
            else:
                print("Нужно ввести номер, а не букву")
        case '5':
            is_running = False
            print("Пока!")
        case _:
            print("Нет такого пункта меню")
