"""
    модуль, который подгружает методы сейва и лоада
"""
import os
from config import FILE_NAME
def load_tasks(file_name=FILE_NAME):
    if not os.path.exists(file_name):
        return []

    tasks = []

    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue
            if "|" in line:
                name, description = line.split("|", 1)
            else:
                name = line
                description = ""

            tasks.append({
                "name": name,
                "description": description
            })

    return tasks


def save_tasks(task_collection, file_name=FILE_NAME):
    with open(file_name, "w", encoding="utf-8") as f:
        for task in task_collection:
            f.write(
                f"{task['name']}|{task['description']}\n"
            )