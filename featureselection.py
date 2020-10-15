import logging
import time

# define logger for this module
logger = logging.getLogger(__name__)

def featureselection():
    logger.info('5 features selected')
    time.sleep(0.1)
    logger.warning('all features are categorical')
