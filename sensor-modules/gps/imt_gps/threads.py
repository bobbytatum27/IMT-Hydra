import threading
import time

class Thread_Subclass(threading.Thread):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        threading.Thread.__init__(self)

    # override run method from threading.Thread class
    def run(self):
        for i in range(100):
            time.sleep(2)
            print(self.a, self.b)


if __name__ == '__main__':
    # init the thread objects, but don't run them yet
    first = Thread_Subclass(0, 5)
    second = Thread_Subclass(1, 3)

    # starts running the thread objects
    first.start()
    second.start()
