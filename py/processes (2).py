import os
import time
import multiprocessing


def func_one():
    print(f"[func_one] ID процесса: {os.getpid()}")
    time.sleep(1)
    return "Результат func_one"


def func_two():
    print(f"[func_two] ID процесса: {os.getpid()}")
    time.sleep(2)
    return "Результат func_two"


def func_three():
    print(f"[func_three] ID процесса: {os.getpid()}")
    time.sleep(3)
    return "Результат func_three"


def func_four():
    print(f"[func_four] ID процесса: {os.getpid()}")
    time.sleep(4)
    return "Результат func_four"


if __name__ == "__main__":
    print(f"[main] ID основного процесса: {os.getpid()}")

    p1 = multiprocessing.Process(target=func_one)
    p2 = multiprocessing.Process(target=func_two)
    p3 = multiprocessing.Process(target=func_three)
    p4 = multiprocessing.Process(target=func_four)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("Все процессы завершены")

#[main] ID основного процесса: 8968
#[func_one] ID процесса: 19912
#[func_two] ID процесса: 24468
#[func_three] ID процесса: 22988
#[func_four] ID процесса: 19604
#Все процессы завершены