#!/usr/bin/python

from multiprocessing import Process

import logging
from logging.handlers import RotatingFileHandler
logger = logging.getLogger('mylogger')
file_handler = RotatingFileHandler('/tmp/multiprocs_noqueue.log', maxBytes=1024 * 1024 * 100, backupCount=20)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

url_list=[1,2,6,20,34,32,44]
process_list = []
def myfunc(x):
    logger.info("Now var is: " + str(x) + ' .')
    print x

if __name__ == '__main__':
    for i in range(len(url_list)):
        p = Process(target=myfunc, args=(url_list[i],))
        p.start()
#        process_list.append(p)

#    for j in process_list:
#        j.join()
