"""Основной файл приложения

    версия 0.0.7

    === Описание ===
        Приложение может сохранять задачи, выдаёт список задач,
        может удалять и редактировать задачи.
        Реализованы функции edited_task и deleted_task,
        цикл while в main, загрузка/сохранение в файл saves.txt.
"""

import os

FILE_NAME = "saves.txt"
collection = []
is_running = True


def load_tasks(file_name=FILE_NAME):
    if not os.path.exists(file_name):
        return []
    with open(file_name, "r", encoding="utf-8") as f:
        tasks = [line.strip() for line in f.readlines() if line.strip()]
    return tasks


def save_tasks(task_collection, file_name=FILE_NAME):
    with open(file_name, "w", encoding="utf-8") as f:
        for task in task_collection:
            f.write(task + "\n")


def show_collection(task_collection=collection):
    if not task_collection:
        print("=" * 45)
        print("Список задач пуст.")
        print("=" * 45)
        return

    print("=" * 45)
    for i, task in enumerate(task_collection, 1):
        print(f"  {i}. {task}")
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
    print("Задача добавлена")


def edited_task(task_collection):
    show_collection(task_collection)

    if not task_collection:
        return

    selected_task = input("Введите номер задачи: ")

    if check_confirm(selected_task, task_collection):
        new_task = input("Введите новое имя задачи: ")

        if len(new_task) < 2:
            print("Название не может быть пустым!")
            return

        task_collection[int(selected_task) - 1] = new_task

        print(f"Задача с номером {selected_task} успешно изменена")
        print("Задача изменена")


def deleted_task(task_collection):
    show_collection(task_collection)

    if not task_collection:
        return

    delete_tasks = input("Введите номер задачи для удаления: ")

    if check_confirm(delete_tasks, task_collection):
        task_collection.pop(int(delete_tasks) - 1)
        print(f"Задача с номером {delete_tasks} успешно удалена")
        print("Задача удалена")


def show_tasks(task_collection):
    show_collection(task_collection)
    print("Список задач показан")


def exit_program():
    global is_running
    is_running = False
    print("До свидания!")


def unknown_command():
    print("Такого пункта нет...")


def main():
    global is_running, collection

    collection = load_tasks()

    while is_running:
        show_menu()
        choice_user = input("Введите ваш выбор: ")

        match choice_user:
            case "1":
                show_tasks(collection)

            case "2":
                add_task(collection)
                save_tasks(collection)

            case "3":
                edited_task(collection)
                save_tasks(collection)

            case "4":
                deleted_task(collection)
                save_tasks(collection)

            case "5":
                save_tasks(collection)
                exit_program()

            case _:
                unknown_command()


if __name__ == "__main__":
    main()
