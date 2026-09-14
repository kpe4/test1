"""Основной файл
ver 0.0.2
"""

is_running = True
collection = []
def show_collection(collection):
    print('='* 30)
    for i, j in enumerate(collection):
        print(f"{i + 1}. {j}")
    print("=" * 30)
while is_running:
    print("1-посмотреть задачу. \n2-добавить задачу \n3-редактировать задачу \n4-удалить \n5-выход")
    clause_user = input("введите свой выбор")
    match str(clause_user):
        case '1':
            show_collection(collection)
        case '2':
            task_name = input("введите название задачи")
            collection.append(task_name)
        case '3':
            show_collection(collection)
            select_edit = int(input("введите номер задачи"))
            if type(select_edit) != str and int(select_edit) > 0 and select_edit <= len(collection) and type(select_edit) == int:
                edit_name = input("новое имя задачи: ")
                collection[select_edit - 1] = edit_name
                print(f"задча '{select_edit}' '{edit_name}' успешно отредактрирована!")
            else:
                print("задачи с таким номером нет")
        case '4':
            show_collection(collection)
            delete_edit = int(input("Введите новый задачи для удаления"))
            if int(delete_edit) > 0 and delete_edit <= len(collection):
                collection.pop(delete_edit - 1)
                print(f"задача '{delete_edit}' успешно удалена")
            else:
                print("задачи с таким номером нет")
        case '5':
            is_running = False
            print('Пока')
        case _:
            print('Нет задач')
