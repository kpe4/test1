"""Основной файл приложения

    версия 0.0.5

    === Описание ===
        Приложение может сохранять задачи, выдаёт список задач,
        может удалять и редактировать задачи.
"""

import processes

collection = ['task1', 'task2']  # список задач
is_running = True


def show_collection():
    print("=" * 45)

    for i, task in enumerate(collection):
        print(i + 1, task)

    print("=" * 45)


def show_menu():
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Редактировать задачу")
    print("4 - Удалить задачу")
    print("5 - Выход")


def check_confirm(select_task, task_list):
    if select_task.isdigit():
        if 0 < int(select_task) <= len(task_list):
            return True
        else:
            print(f"Задачи с номером {select_task} нет в списке")
            return False
    else:
        print("Введите именно номер задачи")
        return False

def add_task(task_collection):
    task_name = input("Введите имя задачи для добавления: ")
    if len(task_name) < 2:
        print("Название не может быть пустым!")
        return
    task_collection.append(task_name)
    processes.show_message("Задача добавлена")

def delete_task(task_collection):
    delete_tasks = input("Введите номер задачи для удаления: ")

    if check_confirm(delete_tasks, task_collection):
        task_collection.pop(int(delete_tasks) - 1)
        print(f"Задача с номером {delete_tasks} успешно удалена")
        processes.show_message("Задача удалена")

def edit_task(task_collection):
    selected_task = input("Введите номер задачи: ")

    if check_confirm(selected_task, task_collection):
        new_task = input("Введите новое имя задачи: ")

        if len(new_task) < 2:
            print("Название не может быть пустым!")
            return

        task_collection[int(selected_task) - 1] = new_task

        print(f"Задача с номером {selected_task} успешно изменена")
        processes.show_message("Задача изменена")

def show_tasks(task_collection):
    show_collection()
    processes.show_message("Список задач показан")

def exit_program():
    global is_running

    is_running = False
    processes.show_message("До свидания!")

def unknown_command():
    processes.show_message("Такого пункта нет...")

def main():
    global is_running
    while is_running:
        show_menu()
        choice_user = input("Введите ваш выбор: ")

        name_file = 'saves.txt'
        file = open(name_file, 'w', encoding='utf-8')
        for line in:

        match choice_user:
            case "1":
                show_tasks(collection)

            case "2":
                add_task(collection)
                name_file = 'saves.txt'
                file = open(name_file, 'w', encoding='utf-8')
                file.write(task.join('\n'))
            case "3":
                show_collection(collection)
                edit_task(collection)

            case "4":
                show_collection(collection)
                delete_task(collection)

            case "5":
                exit_program()

            case _:
                unknown_command()


if __name__ == "__main__":
    main()
