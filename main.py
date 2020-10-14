import multiprocessing
import threading
import logging
from multiprocessing import Queue

import applogger
import dataprocess
import featureselection

# wrapping function required for multiprocessing function which produces logs 
def log_queue_wrap(log_queue):
    # add_formatter is False to leave the formatter to the logger handle the logRecord in the queue
    applogger.add_queuehandler(queue=log_queue, add_formatter=False, rm_otherhanlders=True)
    return dataprocess.dataprocess()

if __name__ == '__main__':
    # output log file
    applogger.add_filehandler(filename='app.log')


    # define queue to store logs, log_queue is reserved for multiprocess log communication
    # It should not be used for other purposes
    log_queue = Queue()

    # log listener process
    log_listener_proc = threading.Thread(target=applogger.log_hanlder, args=(log_queue,))
    log_listener_proc.start()

    p_list = []
    for i in range(2):
        p = multiprocessing.Process(target=log_queue_wrap, args=(log_queue,))
        p.name = 'subprocess {}'.format(str(i))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    log_queue.put_nowait(None)
    log_listener_proc.join()

    featureselection.featureselection()
    
    logging.info('data processing is complete')

