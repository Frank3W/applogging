import logging
import logging.handlers

APPLOG_LEVEL = logging.DEBUG
APPLOG_FILE = 'app.log'

def log_hanlder(queue):
    """Log handling function by a queue.

    Args:
        queue: A queue in multiprocess module that is thread-safe. The get function of the queue supports blocking.

    Returns:
        None
    """
    while True:
        log_record = queue.get()
        if log_record is None:
            break
        else:
            logger = logging.getLogger(log_record.name)
            # Be cautious about the infinite loop that may happen if logger.hanlde invokes thesame queue 
            print(log_record)
            print(log_record.msg)
            logger.handle(log_record)


def get_formatter():
    return logging.Formatter('[%(asctime)s %(processName)s %(threadName)s LOGGER - %(name)s] %(levelname)s - %(message)s')

def add_streamhandler(loggername=None, rm_otherhanlders=False):
    if loggername is None:
        # gets root logger
        logger = logging.getLogger()
    else:
        logger = logging.getLogger(loggername)
    logger.setLevel(APPLOG_LEVEL)

    if rm_otherhanlders:
        logger.handlers = []

    ch = logging.StreamHandler()
    ch.setFormatter(get_formatter())
    logger.addHandler(ch)
    return logger

def add_filehandler(loggername=None, filename=None, rm_otherhandlers=False):
    if loggername is None:
        # gest root logger
        logger = logging.getLogger()
    else:
        logger = logging.getLogger(loggername)
    logger.setLevel(APPLOG_LEVEL)

    if rm_otherhandlers:
        logger.handlers = []

    if filename is not None:
        ch = logging.FileHandler(filename=filename)
    else:
        ch = logging.FileHandler(filename=APPLOG_FILE)
    ch.setFormatter(get_formatter())
    logger.addHandler(ch)
    return logger

def add_queuehandler(queue, loggername=None, add_formatter=True, rm_otherhanlders=False):
    if loggername is None:
        # gest root logger
        logger = logging.getLogger()
    else:
        logger = logging.getLogger(loggername)
    logger.setLevel(APPLOG_LEVEL)

    if rm_otherhanlders:
        logger.handlers = []

    ch = logging.handlers.QueueHandler(queue=queue)
    if add_formatter:
        ch.setFormatter(get_formatter())
    logger.addHandler(ch)
    return logger

