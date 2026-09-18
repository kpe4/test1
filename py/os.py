import time
import os
import sys
import platform
import datetime

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]

now = datetime.datetime.now()
sys_in = sys.path
print(f"{os_name} {os_version} {os_arch} {now.year} {now.month} {now.day} {now.hour}")

os_processor = platform.processor()
os_machine = platform.machine()
os_system = platform.system()
os_version = platform.version()
os_name = platform.python_build()
print(f" {os_processor}\n"
      f" {os_machine}\n"
      f" {os_system}\n"
      f" {os_version}\n"
      f" {os_name}\n")
