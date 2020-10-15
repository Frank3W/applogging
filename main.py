import multiprocessing
import threading
import logging
from multiprocessing import Queue

import applogger
import dataprocess
import featureselection

# wrap the function that invoked in multiprocessing for producing logs: dataprocess.dataprocess 
def log_function_wrap(log_queue):
    # add formatter=False to leave the formatter configuration to the logger that handles logRecords from the queue
    applogger.add_queuehandler(queue=log_queue, add_formatter=False, rm_otherhanlders=True)
    return dataprocess.dataprocess()

if __name__ == '__main__':
    ### set up global log handlers 
    applogger.add_filehandler(filename='app.log')
    applogger.add_streamhandler()

    ### log example: wrapping a function in multiprocessing 

    # define multiprocessing queue to store logs
    # This queue is reserved for log communication in multiprocessing. It should not used in other places.
    log_queue = Queue()

    # log listener thread 
    log_listener_thread = threading.Thread(target=applogger.log_hanlder, args=(log_queue,))
    log_listener_thread.start()

    p_list = []
    for i in range(2):
        p = multiprocessing.Process(target=log_function_wrap, args=(log_queue,))
        p.name = 'subprocess {}'.format(str(i))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    # stop signal for log queue
    log_queue.put_nowait(None)
    log_listener_thread.join()

    ### log example: a function in main process
    featureselection.featureselection()

    logging.info('data processing is complete')

