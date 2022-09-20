import threading
import time

sem = threading.Semaphore()
stop_flag = False


def fun1():
    while not stop_flag:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)


def fun2():
    while not stop_flag:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)


try:
    t1 = threading.Thread(target=fun1)
    t1.start()
    t2 = threading.Thread(target=fun2)
    t2.start()
    while True:
        pass
except KeyboardInterrupt:
    stop_flag = True
    print("KeyboardInterrupt is activate!")
