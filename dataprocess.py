import logging
import time
import random

# define logger for this module
logger = logging.getLogger(__name__)

def dataprocess():
    logger.warning('data input source not updated.')
    logger.info('account data fecthed.')
    time.sleep(random.random())
    logger.error('data incomplete error')
