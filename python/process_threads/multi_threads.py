#!/usr/bin/python

from Queue import Queue
from threading import Thread

q = Queue()
url_list=[1,2,6,20,34,32,44]
thread_list = []
def myfunc(x):
    if x == 20:
        q.put(x+2)
        return q


if __name__ == '__main__':
    for i in range(len(url_list)):
        if q.empty():
            thr = Thread(target=myfunc, args=(url_list[i],))
            thr.start()
            thread_list.append(thr)
        else:
            break
        for j in thread_list:
            j.join()

    for i in range(q.qsize()):
        print q.get()
