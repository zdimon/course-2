import logging


def sum(x,y):
    logger = logging.getLogger(__name__)
    logger.info('fffffffffffffffff')    
    try:
        return x/y
    except Exception, e:
        logger.error('Error %s' % str(e), exc_info=False)
