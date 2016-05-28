import logging
from logger_import import sum

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
handler = logging.FileHandler('hello.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Start reading database')
# read database here

records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here

logger.info('Finish updating records')


try:
    open('/path/to/does/not/exist', 'rb')
except Exception, e:
    logger.error('Failed to open file', exc_info=True)



sum(2,0)






