"""
                    === Функции для добавления, удаления и редактирования задач ===

                                    === Версия приложения: 0.0.9 ===
"""
from
from utils import check_confirm

### Удаление задач
def deleted_task(task_collection):
    show_collection(task_collection)

    if not task_collection:
        return

    delete_task = input(
        "Введите номер задачи для удаления: "
    )

    if check_confirm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)

        print(
            f"Задача с номером {delete_task} успешно удалена"
        )

### Редактирование задач
def edited_task(task_collection):
    show_collection(task_collection)

    if not task_collection:
        return

    selected_task = input("Введите номер задачи: ")

    if check_confirm(selected_task, task_collection):
        new_task = input("Введите новое имя задачи: ").strip()

        if len(new_task) < 2:
            print("Название не может быть пустым!")
            return

        task_collection[int(selected_task) - 1]["name"] = new_task

        print(
            f"Задача с номером {selected_task} успешно изменена"
        )

### Добавление задач
def add_task(task_collection):
    task_name = input("Введите имя задачи для добавления: ").strip()

    if len(task_name) < 2:
        print("Название не может быть пустым!")
        return

    # Сначала добавляем название
    task_collection.append({
        "name": task_name,
        "description": ""
    })

    # Сразу после добавления спрашиваем описание
    description = input(
        "Введите описание задачи (Enter — без описания): "
    ).strip()

    task_collection[-1]["description"] = description

    print("Задача добавлена")