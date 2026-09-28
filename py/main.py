"""Основной файл приложения

    версия 0.0.9

        Приложение может сохранять задачи, выдаёт список задач,
        может добавлять, удалять и редактировать задачи.
        У каждой задачи может быть описание
"""
import storage
from storage import load_tasks
from storage import save_tasks
is_running = True

def show_collection(task_collection):
    if not task_collection:
        print("=" * 45)
        print("Список задач пуст.")
        print("=" * 45)
        return

    print("=" * 45)

    for i, task in enumerate(task_collection, 1):
        print(f"  {i}. {task['name']}")

        if task["description"]:
            print(f"     Описание: {task['description']}")

    print("=" * 45)


def show_menu():
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Редактировать задачу")
    print("4 - Удалить задачу")
    print("5 - Выход")
    print("6 - Изменить описание задачи")


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

def edit_description(task_collection):
    show_collection(task_collection)

    if not task_collection:
        return

    selected_task = input(
        "Введите номер задачи для изменения описания: "
    )

    if check_confirm(selected_task, task_collection):
        task_index = int(selected_task) - 1

        old_description = task_collection[task_index]["description"]

        if old_description:
            print(f"Текущее описание: {old_description}")
        else:
            print("У задачи сейчас нет описания.")

        new_description = input(
            "Введите новое описание (Enter — удалить описание): "
        ).strip()

        task_collection[task_index]["description"] = new_description

        if new_description:
            print(
                f"Описание задачи с номером {selected_task} изменено"
            )
        else:
            print(
                f"Описание задачи с номером {selected_task} удалено"
            )

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
    global is_running

    collection = storage.load_tasks()

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

            case "6":
                edit_description(collection)
                save_tasks(collection)

            case _:
                unknown_command()


if __name__ == "__main__":
    main()
