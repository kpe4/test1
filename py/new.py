# код полчучает данные о компонентах пк, времени. Выводит название системы, версию, архитектуру, дату.
# Генерирует уникальный айди ситемы из названия системы, названия пк, архитектуры и сетевого идентификатора

import sys
import platform
import datetime
import hashlib
import uuid

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0][1]

now = datetime.datetime.now()
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