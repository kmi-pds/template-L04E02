import time
import random
import string
from threading import Thread, Semaphore


N_OF_READERS = random.randint(1, 5)


def write():
    global shared_value

    item = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    print(f"Writing: {item}")
    shared_value = item


def read():
    print(f"Reading: {shared_value}")


def writer():
    while loop_forever:
        time.sleep(random.randint(0, 4))
        write()


def reader():
    global readers_count

    while loop_forever:
        time.sleep(random.randint(0, 4))
        read()


if __name__ == "__main__":
    loop_forever = True
    shared_value = None

    readers_threads = [Thread(target=reader) for _ in range(N_OF_READERS)]
    writers_thread = Thread(target=writer)

    writers_thread.start()

    for thread in readers_threads:
        thread.start()

    time.sleep(10)

    loop_forever = False

    writers_thread.join()

    for thread in readers_threads:
        thread.join()