# Код получает данные о компонентах ПК, времени.
# Выводит название системы, версию, архитектуру, дату.
# Генерирует уникальный ID системы из названия системы,
# названия ПК, архитектуры и сетевого идентификатора.

import os
import sys
import platform
import datetime
import hashlib
import uuid


os_architecture = platform.architecture()[0]  #Получаем архитектуру системы
current_folder = os.getcwd()                 #Получаем текущую папку
python_paths = sys.path                      #Получаем пути поиска модулей Python
os_name = platform.system()                  #Получаем название операционной системы
os_version = platform.version()              #Получаем версию операционной системы
os_arch = platform.architecture()[0]         #Получаем архитектуру системы


now = datetime.datetime.now()  #Получаем текущую дату и время

print("Архитектура:", os_architecture)       #Выводим архитектуру
print("Текущая папка:", current_folder)      #Выводим текущую папку
print("Пути Python:", python_paths)          #Выводим пути Python

print(
    f"{os_name} {os_version} {os_arch} \n"
    f"{now.year} {now.month} {now.day} {now.hour}:{now.minute}"
)  #Выводим информацию о системе, дату и время


info = (
    platform.node()          #Получаем имя компьютера
    + platform.system()      #Получаем название операционной системы
    + platform.machine()     #Получаем тип процессора
    + str(uuid.getnode())    #Получаем сетевой идентификатор
)

system_id = hashlib.sha256(info.encode()).hexdigest()  #Создаём уникальный хеш айди системы

print("ID системы:", system_id)  #Выводим айди системы
