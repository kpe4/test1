# код полчучает данные о компонентах пк, времени. Выводит название системы, версию, архитектуру, дату.
# Генерирует уникальный айди ситемы из названия системы, названия пк, архитектуры и сетевого идентификатора

import os
import sys
import platform
import datetime
import hashlib
import uuid

os_architecture = platform.architecture()[0]
current_folder = os.getcwd()
python_paths = sys.path
os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]

now = datetime.datetime.now()
print("Архитектура:", os_architecture)
print("Текущая папка:", current_folder)
print("Пути Python:", python_paths)
sys_in = sys.path
print(f"{os_name} {os_version} {os_arch} \n {now.year} {now.month} {now.day} {now.hour}:{now.minute}")

info = (
    platform.node()
    + platform.system()
    + platform.machine()
    + str(uuid.getnode())
)
system_id = hashlib.sha256(info.encode()).hexdigest()
print("ID системы:", system_id)