#!/usr/bin/python

from multiprocessing import Process, Queue

q = Queue()
url_list=[1,2,6,20,34,32,44]
process_list = []
def myfunc( x):
    q.put(x+2)
    return q


if __name__ == '__main__':
    for i in range(len(url_list)):
        p = Process(target=myfunc, args=(url_list[i],))
        p.start()
        process_list.append(p)
        for j in process_list:
            j.join()
        
    for i in range(q.qsize()):
        print q.get()
