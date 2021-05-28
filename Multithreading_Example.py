from threading import Thread, Lock

value = 0

def func(lock):

    with lock:
        global value
        copy = value
        copy += 1
        value = copy

if __name__ == "__main__":

    lock = Lock()

    print("Start Value:", value)

    thread1 = Thread(target=func, args=(lock,))
    thread2 = Thread(target=func, args=(lock,))
    thread3 = Thread(target=func, args=(lock,))
    thread4 = Thread(target=func, args=(lock,))
    thread5 = Thread(target=func, args=(lock,))
    thread6 = Thread(target=func, args=(lock,))
    thread7 = Thread(target=func, args=(lock,))
    thread8 = Thread(target=func, args=(lock,))

    threads = [thread1, thread2, thread3, thread4, thread5, thread6, thread7, thread8]

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

    print("End Main:", value)