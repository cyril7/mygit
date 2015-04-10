#!/usr/bin/python

from Queue import Queue
from threading import Thread

import logging
from logging.handlers import RotatingFileHandler
logger = logging.getLogger('mylogger')
file_handler = RotatingFileHandler('/tmp/multithread.log', maxBytes=1024 * 1024 * 100, backupCount=20)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

q = Queue()
url_list=[1,2,6,20,34,32,44]
thread_list = []
def myfunc(x):
    logger.info("Now var is: " + str(x) + ' .')
    if x == 32:
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
